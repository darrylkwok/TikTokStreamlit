# Importing Unofficial TikTok Python SDK
from TikTokApi import TikTokApi as tiktok
# Import JSON for the exporting of data
import json
# Import helper functions
from helpers import process_results

# Get cookies data
verifyFp = "verify_kx9vegow_sGlDMjba_KqiB_4t23_9K1v_yGWgX4Aoybtr"
# Setup the instance 
# use_test_endpoints=True to ensure that we use the non-production endpoints so we can run this multiple times
api = tiktok.get_instance(custom_verifyFp = verifyFp, use_test_endpoints=True)
# Get data by hashtag
trending = api.by_hashtag('ai')

# Process the nested results from the API to a flattened dictionary format
flattened_data = process_results(trending)

# Export data to json
with open('export.json', 'w') as f:
    json.dump(flattened_data, f)

