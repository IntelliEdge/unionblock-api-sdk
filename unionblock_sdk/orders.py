import requests
from .core import OTCApiException, OTCApiOrder
from .constants import OTC_API_URL
from .auth import get_access_token, get_signature
import time

def quote(username, password, base_token='USDT', quote_token='USD', quantity=1.0):
    access_token = get_access_token(username, password)

    url = f'{OTC_API_URL}/orders/quote/'
    
    data = {
        "base_token": base_token,
        "quote_token": quote_token,
        "quantity": quantity,
        "side": "sell"
    }

    headers={
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        return OTCApiOrder.from_json(response.json())
    else:
        raise OTCApiException(f'Error: Quote request failed. Status code: {response.status_code}. Response: {response.text}')


def execute(username, password, api_key, api_secret_key, order_id):
    access_token = get_access_token(username, password)

    url = f'{OTC_API_URL}/orders/execute/'

    data = {
        "order_id": order_id,
    }

    timestamp = str(int(time.time()))
    signature = get_signature(api_secret_key, url, 'POST', data, timestamp)
    headers = {
        'Authorization': ('Bearer ' + access_token),
        'X-Apikey': api_key,
        'X-Signature': signature,
        'X-Timestamp': timestamp,
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return OTCApiOrder.from_json(response.json())
    else:
        raise OTCApiException(f'Error: Order execute request failed. Status code: {response.status_code}. Response: {response.text}')


