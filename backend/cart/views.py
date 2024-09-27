from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import status
from .models import Cart, CartItem
from base.models import Item

class AddItemToCart(GenericAPIView):
    def post(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        user_id = request.user.id
        print(user_id)
        if Item.objects.filter(id=pk).exists:
            item = Item.objects.get(id=pk)
            cart_item = CartItem.objects.get(item=item, "")
        return Response({"message": "Item does not exist"})
