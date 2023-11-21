# Importing your classes and requests module
from unionblock_sdk import OTCApi
from unionblock_sdk.core import OTCApiException
from examples_config import *


# Creating an instance of OTCApi with your credentials
otc_api = OTCApi(username=USERNAME, password=PASSWORD, api_key=API_KEY, api_secret_key=API_SECRET_KEY)

try:
    txs = otc_api.list_transactions()
    print(f"Exisitng transactions:")
    for t in txs:
        print(f"- Tx ID: {t.id}")
        print(f"- Tx Order ID: {t.order.order_id}")
        print(f"- Tx Base Token: {t.order.base_token}")
        print(f"- Tx Quote Token: {t.order.quote_token}")
        print(f"- Tx Quantity: {t.order.quantity}")
        # ... (print other fields as needed)
        print('------------------------------')

except OTCApiException as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

