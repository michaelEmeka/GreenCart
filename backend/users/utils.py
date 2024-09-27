import random
from django.core.mail import EmailMessage
from django.conf import settings
from .models import OneTimePassword

def otpGen():
    otp = ""
    for i in range(6):
        otp += str(random.randint(0,9))
    return otp

def send_code_to_user(user):
    
    Subject = "One Time passcode for Email Verification" 
    otp_code = otpGen()
    print(otp_code)
    #user = CustomUser.objects.get(email=email)
    current_site = "todo.com"
    email_body = f"Hi {user.business_name}, thanks for signing up on {current_site}, your OTP is {otp_code}"
    from_email = settings.DEFAULT_FROM_EMAIL
    
    OneTimePassword.objects.create(user=user, code=otp_code)
    
    email = EmailMessage(subject=Subject, body=email_body, from_email=from_email, to=[user.email])
    email.send(fail_silently=True)

def send_email(data):
    email = EmailMessage(
        subject=data["email_subject"],
        body=data["email_body"],
        from_email=settings.EMAIL_HOST_USER,
        to=data["to_email"]
        )
    email.send()