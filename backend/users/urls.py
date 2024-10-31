from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("signup/", views.RegisterUserView.as_view(), name="signup_user"),
    path("verify-user/", views.VerifyUserEmail.as_view(), name="otp_verification"),
    path("resend-otp/", views.ResendOTP.as_view(), name="resend_otp"),
    path("login/", views.LoginUserView.as_view(), name="login-user"),
    path(
        "password-reset/", views.ResetUserPassword.as_view(), name="reset_user_password"
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        views.PasswordResetConfirm.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "set-new-password/", views.SetUserPassword.as_view(), name="set_user_password"
    ),
    path("logout/", views.LogoutUser.as_view(), name="logout_user"),
    path("user-detail/", views.UserDetail.as_view(), name="user_detail"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
