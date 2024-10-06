from rest_framework import serializers
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework.exceptions import AuthenticationFailed
from .models import CartItem, Cart, Checkout
from users.models import User
from .payments import initPayment
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
    #total = serializers.IntegerField(write_only=True)
    phone = serializers.IntegerField(write_only=True, required=False)
    address = serializers.CharField(write_only=True, required=False)
    redirect_success = serializers.CharField(write_only=True)
    class Meta:
        model = Checkout
        fields = ["address", "phone", "redirect_success"]

    def validate(self, attrs):
        user = User.objects.get(id=self.context["request"].user.id)
        cart = user.carts.get(is_closed=False)
        
        address = attrs.get("address")
        phone = attrs.get("phone")
        redirect_success = attrs["redirect_success"]\
        
        attrs["business_name"] = user.business_name
        attrs["total"] = cart.get_cart_total()
        attrs["email"] = user.email

        if not redirect_success:
            raise serializers.ValidationError("Redirection link not provided")
        if not(address or user.address):
            raise serializers.ValidationError("No user address available")
        else:
            attrs["address"] = address or user.address
        if not(phone or user.phone):
            raise serializers.ValidationError("No user phone number available")
        else:
            attrs["phone"] = phone or user.phone
        
        return attrs
    
    def create(self, validated_data):

        data = initPayment(validated_data)
        print((data))
        return data