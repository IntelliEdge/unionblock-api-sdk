import requests
import json
import sys
import json, hmac, hashlib, time, base64
import time

timestamp = str(int(time.time()))
url = ''
method=''
private_key = ''
data = ''
jwt = ''
if len(sys.argv) == 7 :
    url = sys.argv[1]
    method = sys.argv[2]
    data = sys.argv[3]
    apikey = sys.argv[4]
    secret = sys.argv[5]
    jwt = sys.argv[6]
else:
    print("No arguments provided.")


# Convert data to JSON
message = timestamp + method + url + data
signature = hmac.new(secret.encode('utf-8'), message.encode('utf-8'), digestmod=hashlib.sha256).digest()

# Send the request with the signature and JSON data
headers = {
    'Authorization': ('Bearer ' + jwt),
    'X-Apikey': apikey,
    'X-Signature': signature.hex(),
    'X-Timestamp': timestamp,
    'Content-Type': 'application/json',
}

if method == 'POST':
    print()
    print('POST ' + url)
    response = requests.post(url, headers=headers, data=data)
elif method == 'PUT':
    print()
    print('PUT ' + url)
    response = requests.put(url, headers=headers, data=data)


print()
print('Headers:')
print(headers)
print()
print('Payload:')
print(data)
print()
print('Response:')
print(response.text)
print()

