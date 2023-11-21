# Importing your classes and requests module
from unionblock_sdk import OTCApi
from examples_config import USERNAME

otc_api = OTCApi(username=USERNAME)
if otc_api.username == 'TEST':
    print(f'unionblock_sdk successfuly installed.')
else:
    print('Something went wrong')

