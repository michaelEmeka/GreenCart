from rest_framework import serializers
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework.exceptions import AuthenticationFailed
from .models import CartItem, Cart, Shipment
#from .utils import send_email

class defaultNull(serializers.Serializer):
    pass

class ListOpenCartItemsSerializer(serializers.ModelSerializer):
    cart_total = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = CartItem
        fields = ["cart", "item", "quantity", "get_cartitem_total", "cart_total"]
    
    def get_cart_total(self, instance):
        return instance.cart.get_cart_total()

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ["total", "address", ]