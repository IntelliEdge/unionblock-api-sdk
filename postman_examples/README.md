# UnionBlock SDK

The UnionBlock SDK provides a convenient way to interact with the UnionBlock API for OTC (Over-the-Counter) trading.

## Installation

To use the UnionBlock SDK in your project, follow these steps:

### 1. Prerequisites

Make sure you have Python 3.X.X installed on your machine. You can download Python from [python.org](https://www.python.org/).

### 2. Setup and activate virtualenv (Optional but recommended)

It's a good practice to use a virtual environment to isolate your project's dependencies. 

### 3. Clone the Repository

```
git clone git@github.com:IntelliEdge/otc-api.git
cd otc_client_utils/unionblock_sdk/
```

### 4. Install Dependencies and Build the SDK

```
python setup.py sdist
pip install dist/unionblock-sdk-1.0.0.tar.gz
```

### 6. Verify Installation

```
python examples/verify_sdk.py
```

## Usage

To use the UnionBlock SDK in your project, you can import it and setup as follows:

```
from unionblock_sdk import OTCApi

# Initialize the API with your credentials
otc_api = OTCApi(username='your_username', password='your_password', api_key='your_api_key', api_secret_key='your_api_secret_key')
```


To request for price use:

```
# Make quoting requests
quote = otc_api.quote_order(base_token='USDT', quote_token='USD', quantity='10.000000')
```


Quote orders can be executed as:

```
# Execute quote order
order = otc_api.execute_order(order_id=quote.order_id)
```


To list all transacations use:

```
# List transactions with:
txs = otc_api.list_transactions()
```


To list single transaction use:

```
# Get transaction with:
tx = otc_api.get_transactions(tx_id='your_transaction_id')
```

Please find example code in folder otc_client_utils/unionblock_sdk/examples/*

## License

This project is licensed under the MIT License


