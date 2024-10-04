from rest_framework import serializers
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework.exceptions import AuthenticationFailed
from .models import CartItem
#from .utils import send_email

class defaultNull(serializers.Serializer):
    pass

class ListOpenCartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"