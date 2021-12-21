# Importing Unofficial TikTok Python SDK
from TikTokApi import TikTokApi as tiktok
# Import JSON for the exporting of data
import json
# Import helper functions
from helpers import process_results
import pandas as pd
# Import sys library, to extract arguments
import sys


def get_data(hashtag):
    # Get cookies data
    verifyFp = "verify_kx9vegow_sGlDMjba_KqiB_4t23_9K1v_yGWgX4Aoybtr"
    # Setup the instance 
    # use_test_endpoints=True to ensure that we use the non-production endpoints so we can run this multiple times
    api = tiktok.get_instance(custom_verifyFp = verifyFp, use_test_endpoints=True)
    # Get data by hashtag
    trending = api.by_hashtag(hashtag)

    # Process the nested results from the API to a flattened dictionary format
    flattened_data = process_results(trending)

    # Convert data into a dataframe
    df = pd.DataFrame.from_dict(flattened_data, orient='index')
    # Export the converted dataframe into a csv file
    df.to_csv('tiktokdata.csv', index=False)

# To protect this script to be executed at import time
# if this module is the main program -> __name__ = '__main__'
# if this module is imported --> __name__ = 'tiktok'
if __name__ == '__main__':
    # Take the second argument and pass it in as a parameter to the get_data function
    get_data(sys.argv[1])
    print(sys.argv)