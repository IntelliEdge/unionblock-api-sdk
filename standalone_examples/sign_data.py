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
if len(sys.argv) == 3 :
    data = sys.argv[1]
    private_key = sys.argv[2]
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

print(signature.hex())
