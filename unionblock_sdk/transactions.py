import requests

from .auth import get_access_token
from .core import OTCApiException, OTCApiTransaction
from .constants import OTC_API_URL

def get(username, password, tx_id):
    access_token = get_access_token(username, password)

    url = f'{OTC_API_URL}/transactions/{tx_id}/'

    headers={
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return OTCApiTransaction.from_json(response.json())
    else:
        raise OTCApiException(f'Error: Transaction get failed. Status code: {response.status_code}. Response: {response.text}')

def list(username, password):
    access_token = get_access_token(username, password)

    url = f'{OTC_API_URL}/transactions/'

    headers={
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return OTCApiTransaction.from_json(response.json())
    else:
        raise OTCApiException(f'Error: Transaction get failed. Status code: {response.status_code}. Response: {response.text}')

