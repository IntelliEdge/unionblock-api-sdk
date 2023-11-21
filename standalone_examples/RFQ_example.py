import requests
import json
import sys

OTC_API_URL='https://api.unionblock.pro/api/v1'

script_name = sys.argv[0]
if len(sys.argv) != 6:
    print(f"Usage: python3 {script_name} <username> <password> <base_token> <quote_token> <quantity>")
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
base_token = sys.argv[3]
quote_token = sys.argv[4]
quantity = sys.argv[5]

auth_response = requests.post(f'{OTC_API_URL}/auth/', json={
    "username": username,
    "password": password
  })


if auth_response.status_code == 200:
    auth_response_json = auth_response.json()
    access_token = auth_response_json.get('access')
else:
    print(f'Error: Please enter valid credentials.')
    sys.exit(1)


rfq_response = requests.post(f'{OTC_API_URL}/orders/quote/', 
  headers={
    'Authorization': f'Bearer {access_token}'
  }, json={
    "base_token": base_token,
    "quote_token": quote_token,
    "quantity": quantity,
    "side": "sell"
  })
 
if rfq_response.status_code == 201:
    rfq_response_json = rfq_response.json()
    print(rfq_response_json)
else:
    print(f'Error: {rfq_response.status_code} - {rfq_response.text}')

