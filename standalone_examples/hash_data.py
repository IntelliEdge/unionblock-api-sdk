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
if len(sys.argv) == 5 :
    url = sys.argv[1]
    method = sys.argv[2]
    data = sys.argv[3]
    secret = sys.argv[4]
else:
    print("No arguments provided.")


# Convert data to JSON
message = timestamp + method + url + data
signature = hmac.new(secret.encode('utf-8'), message.encode('utf-8'), digestmod=hashlib.sha256).digest()

print(message)
print(timestamp)
print(signature.hex())
