import requests
import json
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import sys

url = ''
method=''
private_key = ''
data = ''
jwt = ''
if len(sys.argv) == 6 :
    url = sys.argv[1]
    method = sys.argv[2]
    data = sys.argv[3]
    private_key = sys.argv[4]
    jwt = sys.argv[5]
else:
    print("No arguments provided.")

# Load the private key from file
with open(private_key, 'rb') as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None,
        backend=default_backend()
    )

# Get the public key from the private key
#public_key = private_key.public_key()

# Convert data to JSON
json_data = data.encode('utf-8')

# Sign the data using the private key
signature = private_key.sign(
    json_data,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Load the public key from file
#with open('/home/ubuntu/Desktop/OTCREAL/OTC-API/public_key.pem', 'rb') as f:
#    public_key = serialization.load_pem_public_key(
#        f.read(),
#        backend=default_backend()
#    )

# Verify the signature using the loaded public key
#try:
#    public_key.verify(
#        signature,
#        json_data,
#        padding.PSS(
#            mgf=padding.MGF1(hashes.SHA256()),
#            salt_length=padding.PSS.MAX_LENGTH
#        ),
#        hashes.SHA256()
#    )
#    print("Signature is valid.")
#except InvalidSignature:
#    print("Signature is invalid.")

# Send the request with the signature and JSON data
headers = {
    'Authorization': ('Bearer ' + jwt),
    'X-Signature': signature.hex(),
    'Content-Type': 'application/json',
}

if method == 'POST':
    print()
    print('POST ' + url)
    response = requests.post(url, headers=headers, data=json_data)
elif method == 'PUT':
    print()
    print('PUT ' + url)
    response = requests.put(url, headers=headers, data=json_data)


print()
print('Headers:')
print(headers)
print()
print('Payload:')
print(json_data)
print()
print('Response:')
print(response.text)
print()

