import requests
from datetime import datetime, timezone
from token_api import api_token

username = 'xxxxxxx'
password = 'xxxx#xxxxxx'

current_date = datetime.now()
formatted_date = current_date.strftime('%Y-%m-%d')
url = f'https://xxxxxxxxx={formatted_date}'  

def create_bucket(url, api_token, username, password):
  headers = {
  'access-token': api_token
  }
  response = requests.get(url, headers=headers, auth=(username, password))
  if response.status_code == 200:
      bucket = response.json()
      if 'bucketId' in bucket:
            return bucket['bucketId']
      else:
            print("bucketId not found in the response.")
            return bucket
      #return bucket
  else:
    print(f"Request failed with status code: {response.status_code}")
    return response.json

bucket_id = create_bucket(url, api_token, username, password)
#print("bucketId =", bucket_id)
#bucketId = 