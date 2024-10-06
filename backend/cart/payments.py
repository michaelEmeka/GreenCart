import requests
import json
import os
import uuid
from dotenv import load_dotenv

load_dotenv()


def initPayment(data):
    endpoint = 'https://api.flutterwave.com/v3/payments'
    SEC_KEY = os.getenv("FLW_SECRET_KEY")
    data = {
        "tx_ref": str(uuid.uuid4()),
        "amount": str(data["total"]),
        "currency": "NGN",
        "redirect_url": str(data["redirect_success"]),
        "customer": {
            "email": data["email"],
            "name": data["business_name"],
            "phonenumber": data["phone"]
            },
        "customizations": {
            "title": "Your Green Cart Is Ready!",
            "colour": "#217103"
            }
    }
    headers = {
        "Authorization": f"Bearer {SEC_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(endpoint, data=json.dumps(data), headers=headers)
    return response.json()