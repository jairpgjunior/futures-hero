import os
from binance.client import Client

# Paste the following into your Default Shell
"""
export API_OWNER="your_binance_username"
export API_KEY="your_api_key"
export API_SECRET="your_secret_key"
"""

# Get environment variables
api_owner   = os.environ.get('API_OWNER')
api_key     = os.environ.get('API_KEY')
api_secret  = os.environ.get('API_SECRET')

# Check Your Environment
print("API OWNER        :   " + api_owner)
print("API Key          :   " + api_key)
print("API Secret Key   :   " + api_secret)

# client = Client(keys.api_key, keys.api_secret)