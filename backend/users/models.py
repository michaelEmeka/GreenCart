from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from base.models import ItemTag
from .managers import CustomUserManager
from datetime import timedelta
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=255, unique=True)
    business_name= models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=30, blank=True, null=True)
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
    
    def tokens(self):
        refresh=RefreshToken.for_user(self)
        return{
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }


class OneTimePassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)
    time_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.business_name}-passcode"

    @property
    def is_expired(self):
        current_time = timezone.now()
        return (current_time - self.time_expired).total_seconds() > 300
