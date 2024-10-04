from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
# from rest_framework.status import status
from .models import Cart, CartItem
from base.models import Item
from .serializers import defaultNull, ListOpenCartItemsSerializer
from users.models import User
from django.shortcuts import get_object_or_404



class ListOpenCartItems(ListAPIView):
    serializer_class = ListOpenCartItemsSerializer
    
    def get_queryset(self):
        user = self.request.user
        #print(type(user))
        return user.carts.get(is_closed=False).cart_items.all()

class ModifyCartItem(GenericAPIView):
    """
    Modify cart item, by updating cart item quantity / creating cart item if cart item is non existent
    Add to cart
    Delete from cart
    Update Cart
    pk: item id
    """
    serializer_class = defaultNull
    def post(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        action = request.data.get("action")
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        # print(user_id)
        if Item.objects.filter(id=pk).exists:
            item = Item.objects.get(id=pk)
            cart, created = Cart.objects.get_or_create(user=user, is_closed=False)
            print(item)
            if action == "increase":
                print(item)
                
                cart_item, created = CartItem.objects.get_or_create(item=item, cart=cart)
                if not created: 
                    if cart_item.quantity < cart_item.item.quantity:
                        cart_item.quantity += 1
                        cart_item.save()
                        return Response({"message": "Item successfully added to cart"})
                    else:
                        return Response({"message": "Cart Item cannot exceed available item quantity"})
                return Response({"message": "Item successfully added to cart"})
                    
            elif action == "decrease":
                cart = get_object_or_404(Cart, user=user, is_closed=False)
                cart_item = get_object_or_404(CartItem, item=item, cart=cart)
                if cart_item.quantity <= 1:
                    cart_item.delete()
                    return Response({"message": "Item successfully removed from cart"})
                else:
                    cart_item.quantity -=1
                    cart_item.save()
                    return Response({"message": "Item successfully removed from cart"})
            else:
                return Response({"message": "Invalid action"})

        return Response({"message": "Item does not exist"})

class RemoveFromCart(GenericAPIView):
    """
    Remove from cart view, takes in cart_item id, and deletes cart_item
    pk: cart_item id
    """
    serializer_class = defaultNull
    def delete(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        if CartItem.objects.filter(id=pk).exists:
            user = User.objects.get(id=request.user.id)
            cart = Cart.objects.get(user=user, is_closed=False)
            cart_item = CartItem.objects.get(id=pk, cart=cart)
            cart_item.delete()
            return Response({"message": "Item successfully deleted from cart"})
        return Response({"message": "Item does not exist in cart"})