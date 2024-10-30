import requests
import json
import os
#import uuid
from dotenv import load_dotenv

load_dotenv()


def CashPay(checkout, redirect):
    endpoint = 'https://api.flutterwave.com/v3/payments'
    SEC_KEY = os.getenv("FLW_SECRET_KEY")
    data = {
        "tx_ref": str(checkout.transaction_id),
        "amount": str(checkout.cart.get_cart_total()),
        "currency": "NGN",
        "redirect_url": redirect,
        "customer": {
            "email": checkout.cart.user.email,
            "name": checkout.cart.user.email,
            "phonenumber": str(checkout.phone),
        },
        "customizations": {"title": "Your Green Cart Is Ready!", "colour": "#217103"},
    }
    headers = {
        "Authorization": f"Bearer {SEC_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(endpoint, data=json.dumps(data), headers=headers)
    return response.json()
