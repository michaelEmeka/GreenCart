from rest_framework import serializers
from .models import User, OneTimePassword
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import smart_str, smart_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework.exceptions import AuthenticationFailed
from .utils import send_email


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=60, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=60, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password", "password2"]

    def validate(self, attrs):
        password = attrs["password"]
        password2 = attrs["password2"]

        if password != password2:
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create_user(**validated_data)
        return user


class VerifyUserSerializer(serializers.Serializer):
    otp = serializers.CharField(required=True)

    def validate(self, attrs):
        otp = attrs["otp"]
        otp_obj = OneTimePassword.objects.filter(code=otp).first()

        user = otp_obj.user
        # Check if the OTP exists
        # Get the first matching OTP object
        if otp_obj:
            if not user.is_verified:
                if not otp_obj.is_expired:
                    user.is_verified = True
                    user.save()
                    return {"message": "User verified successfully"}
                raise serializers.ValidationError("The provided code is expired")
            raise serializers.ValidationError("This user is verified, please login")
        raise serializers.ValidationError("The provided code is invalid")


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=6)
    password = serializers.CharField(max_length=68, write_only=True)
    access_token = serializers.CharField(max_length=255, read_only=True)
    refresh_token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "access_token", "refresh_token"]

    def validate(self, attrs):
        # attrs: request.data passed
        # self: used to get any other object passsed
        email = attrs["email"]
        password = attrs.get("password")
        print(email, password)
        request = self.context.get("request")
        # print(request.data)
        user = authenticate(request=request, email=email, password=password)

        if not user:
            # user doesn't exist
            raise AuthenticationFailed("Invalid credentials try again")

        if not user.is_verified:
            # user not verified
            raise AuthenticationFailed("User email is not verified")

        user_tokens = user.tokens()
        return {
            "email": email,
            "first_name": user.first_name,
            "access_token": str(user_tokens.get("access")),
            "refresh_token": str(user_tokens.get("refresh")),
        }


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ["email"]

    def validate(self, attrs):
        email = attrs["email"]
        request = self.context["request"]

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            site_domain = get_current_site(request).domain
            relative_link = reverse(
                "password_reset_confirm", kwargs={"uidb64": uidb64, "token": token}
            )
            absolute_link = f"{site_domain}{relative_link}"
            email_body = (
                f"Hi click on the link below to reset your password \n {absolute_link}"
            )
            data = {
                "email_subject": "Reset your password",
                "email_body": email_body,
                "to_email": [user.email],
            }
            send_email(data)
            return super().validate(attrs)
        raise serializers.ValidationError("User does not exist")


class SetUserPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=100, min_length=8, write_only=True)
    confirm_password = serializers.CharField(
        max_length=100, min_length=8, write_only=True
    )
    uidb64 = serializers.CharField(write_only=True)
    token = serializers.CharField(write_only=True)

    def validate(self, attrs):
        try:
            password = attrs["password"]
            confirm_password = attrs["confirm_password"]
            uidb64 = attrs["uidb64"]
            token = attrs["token"]

            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed("Reset link is invalid or has expired", 401)
            if password != confirm_password:
                raise AuthenticationFailed("User passwords do not match")
            user.set_password(password)
            user.save()
            return user
        except Exception as e:
            raise AuthenticationFailed("Reset link is invalid or has expired")

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "address", "phone", "interest_tags"]