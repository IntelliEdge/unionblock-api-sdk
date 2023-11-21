# Importing your classes and requests module
from unionblock_sdk import OTCApi
from unionblock_sdk.core import OTCApiException
from examples_config import *


# Creating an instance of OTCApi with your credentials
otc_api = OTCApi(username=USERNAME, password=PASSWORD, api_key=API_KEY, api_secret_key=API_SECRET_KEY)


try:
    quote = otc_api.quote_order(base_token='USDT', quote_token='USD', quantity='11.110000')
    print(f"Quote order:")
    print(f"- Order ID: {quote.order_id}")
    print(f"- Base Token: {quote.base_token}")
    print(f"- Quote Token: {quote.quote_token}")
    print(f"- Quantity: {quote.quantity}")
    print(f"- Side: {quote.side}")
    # ... (print other fields as needed)
    print()
    print()


    order = otc_api.execute_order(order_id=quote.order_id)
    print(f"Executed order:")
    print(f"- Order ID: {order.order_id}")
    print(f"- Base Token: {order.base_token}")
    print(f"- Quote Token: {order.quote_token}")
    print(f"- Quantity: {order.quantity}")
    print(f"- Side: {order.side}")
    # ... (print other fields as needed)
    print()
    print()

except OTCApiException as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

