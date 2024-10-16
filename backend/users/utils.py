import random
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .models import OneTimePassword
import smtplib
import logging

logger = logging.getLogger(__name__)


def otpGen():
    otp = ""
    for i in range(6):
        otp += str(random.randint(0, 9))
    return otp


def send_code_to_user(user):

    Subject = "One Time Passcode for Email Verification"
    otp_code = otpGen()
    print(otp_code)
    # user = CustomUser.objects.get(email=email)
    current_site = "greencart.com"
    email_body = f"Hi {user.first_name}, thanks for signing up on {current_site}, your OTP is {otp_code}"
    from_email = settings.DEFAULT_FROM_EMAIL
    print(from_email)
    OneTimePassword.objects.create(user=user, code=otp_code)

    # send_mail(
    # Subject, email_body, from_email, [user.email]
    # )
    try:
        email = EmailMessage(
            subject=Subject,
            body=email_body,
            from_email=from_email,
            to=[str(user.email)],
        )
        email.send(fail_silently=False)
    except Exception as e:
        logger.error(f"Error sending email: {e}")
    print(f"I attempted send to: {user.email}")


def send_email(data):
    email = EmailMessage(
        subject=data["email_subject"],
        body=data["email_body"],
        from_email=settings.EMAIL_HOST_USER,
        to=data["to_email"],
    )
    print(data["to_email"])
    email.send()
