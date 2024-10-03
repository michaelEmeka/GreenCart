from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
# from rest_framework.status import status
from .models import Cart, CartItem
from base.models import Item
from .serializers import defaultNull
from .models import User

class AddItemToCart(GenericAPIView):
    serializer_class = defaultNull
    def get(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        # print(user_id)
        if Item.objects.filter(id=pk).exists:
            item = Item.objects.get(id=pk)
            print(item)
            cart, created = Cart.objects.get_or_create(user=user, is_closed=False)
            if CartItem.objects.filter(item=item, cart=cart).exists():
                cart_item = CartItem.objects.get(item=item, cart=cart)
                cart_item.quantity += 1
                cart_item.save()
            else:
                cart_item = CartItem.objects.create(item=item, cart=cart)
                cart_item.quantity += 1
                cart_item.save()
            return Response({"message": "Item successfully added to cart"})
        return Response({"message": "Item does not exist"})
