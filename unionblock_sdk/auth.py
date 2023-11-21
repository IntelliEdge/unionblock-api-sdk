import requests
from .core import OTCApiException
from .constants import OTC_API_URL
import hmac, hashlib

def get_access_token(username, password):
    
    url = f'{OTC_API_URL}/auth/'
    
    data = {
        "username": username,
        "password": password
    }

    auth_response = requests.post(url, json=data)
    if auth_response.status_code == 200:
        auth_response_json = auth_response.json()
        return auth_response_json.get('access')
    else:
        raise OTCApiException(f'Error: Authentication failed. Status code: {auth_response.status_code}')

def get_signature(api_secret_key, url, method, data, timestamp):
    try:
        # make signature
        message = timestamp + method + url + str(data)
        signature = hmac.new(api_secret_key.encode('utf-8'), message.encode('utf-8'), digestmod=hashlib.sha256).digest()
        return signature.hex()
    except:
        raise OTCApiException(f'Error: Signing request failed.')
