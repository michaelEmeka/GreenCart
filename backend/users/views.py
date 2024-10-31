from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .utils import send_code_to_user
from .serializers import *
from .models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


class RegisterUserView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    def post(self, request):
        data = request.data

        # Checks if user exists in database
        if User.objects.filter(email=data["email"], is_verified=False).exists():
            return Response(
                {"message": "User with this email already exists, kindly verify"},
                status=status.HTTP_409_CONFLICT,
            )

        # Create user for non existent user
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            user = serializer.save()
            # send email function user['email']
            send_code_to_user(user)
            return Response(
                {
                    "data": serializer.data,
                    "message": f"Hi, {user.first_name}. Thanks for signing up, a passcode has been sent to your email",
                },
                status=status.HTTP_201_CREATED,
            )
            print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyUserEmail(GenericAPIView):
    serializer_class = VerifyUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResendOTP(GenericAPIView):
    serializer_class = defaultNull
    def post(self, request):
        email = request.data["email"]
        user = User.objects.filter(email=email).first()
        if user:
            send_code_to_user(user)
            return Response({"message": "otp resent"}, status=status.HTTP_200_OK)
        return Response({"message": "bad request"}, status=status.HTTP_400_BAD_REQUEST)


class LoginUserView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ResetUserPassword(GenericAPIView):
    serializer_class = PasswordResetRequestSerializer
    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid(raise_exception=True):
            return Response(
                {"message": "check your email for reset verification link"},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirm(GenericAPIView):
    """
    The PasswordResetConfirm class in the provided code snippet is a view that handles the confirmation of a password reset request. It is designed to handle GET requests and expects two parameters in the URL: `uidb64` and `token`.
    Args:
        uidb64: encoded user id
        token: password reset token
    """
    serializer_class = defaultNull
    def get(self, request, uidb64, token):
        try:
            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)
            # check if encoded user is the same as tokenized user
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response(
                    {"message": "token is invalid or has expired"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            return Response(
                {"message": "user is valid", "uidb64": uidb64, "token": token},
                status=status.HTTP_200_OK,
            )

        except DjangoUnicodeDecodeError:
            return Response(
                {"message": "token is invalid or has expired"},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class SetUserPassword(GenericAPIView):
    """
    The `SetUserPassword` class in the provided code snippet is a view for setting a new password for a user. It is designed to handle PATCH requests and expects a request containing data necessary to set a new password for a user.

    Args:
        self: view instance
        request: request object
    """
    serializer_class = SetUserPasswordSerializer
    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"message": "Password reset successfully"})


class LogoutUser(GenericAPIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"message": "User successfully logged out"},
                status=status.HTTP_205_RESET_CONTENT,
            )
        except Exception as e:
            raise e

# Get user
class UserDetail(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserDetailSerializer
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
