from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy

class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            print("I'm in the validator")
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Please enter a  valid email address"))
    def create_user(self, email, business_name, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        else:
            email = self.normalize_email(email)
            self.email_validator(email)
        if not business_name:
            raise ValueError("Business name must be provided")
        user = self.model(email=email, business_name=business_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, business_name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_verified", True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser set to True")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff set to True")
        if extra_fields.get("is_verified") is not True:
            raise ValueError("Superuser must have is_verified set to True")
        user = self.create_user(email, business_name, password, **extra_fields)
        return user