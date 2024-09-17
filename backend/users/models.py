from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from base.models import ItemTag
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=255, unique=True)
    business_name= models.CharField(max_length=30, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    interest_tags = models.ManyToManyField(ItemTag, related_name="users")
    
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["business_name"]
    
    
    def __str__(self):
        return self.email