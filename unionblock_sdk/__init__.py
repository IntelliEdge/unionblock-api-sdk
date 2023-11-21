from .orders import execute as order_execute_exe, quote as quote_order_exe
from .transactions import get as get_transaction_exe, list as list_transactions_exe

class OTCApi:

    # Example usage:
    # otc_api = OTCApi(username='your_username', password='your_password', api_key='your_api_key', api_secret_key='your_api_secret_key')
    def __init__(self, username=None, password=None, api_key=None, api_secret_key=None):
        self.username = username
        self.password = password
        self.api_key = api_key
        self.api_secret_key = api_secret_key


    # Example usage:
    # order = otc_api.quote_order(base_token='USDT', quote_token='USD', quantity=1.0)
    def quote_order(self, base_token='USDT', quote_token='USD', quantity=1.0):
        return quote_order_exe(self.username, self.password, base_token, quote_token, quantity)


    # Example usage:
    # order = otc_api.execute_order('your_quote_order_id')
    def execute_order(self, order_id):
        return order_execute_exe(self.username, self.password, self.api_key, self.api_secret_key, order_id)


    # Example usage:
    # tx = otc_api.get_transaction_exe('your_tx_id')
    def get_transaction(self, tx_id):
        return get_transaction_exe(self.username, self.password, tx_id)


    # Example usage:
    # tx = otc_api.list_transactions('your_tx_id')
    def list_transactions(self):
        return list_transactions_exe(self.username, self.password)

