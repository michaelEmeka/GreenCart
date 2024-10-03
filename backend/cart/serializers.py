from rest_framework import serializers
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework.exceptions import AuthenticationFailed
#from .utils import send_email

class defaultNull(serializers.Serializer):
    pass