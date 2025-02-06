import requests
from datetime import datetime, timezone

url = 'https://xxxxxuj4.'
username = 'dixxxxxx'
password = 'Fxxxxxxxxx'

#time_now = datetime.now(timezone.utc)
def get_token(username, password, url):
  response = requests.get(url, auth=(username, password))
  if response.status_code == 200:
  # Parse the response to extract the token (assuming JSON format)
    #token = response.json().get("access_token")
    acc_token = response.json()
    token = acc_token['accessToken']
    return token
  else:
    print("Token not found in the response.")
    return None
  

api_token = get_token(username, password, url)
#print("token =", api_token)


'''def create_bucket(url2, api_token):
  headers = {
  "Authorization": 'api_token',
  "Content-Type": 'application/json'
}
  response = requests.get(url2, headers=headers)
  if response.status_code == 200:
    bucket_id = response.json()
    bucket = bucket_id['BucketID']
    return bucket
  else:
    print("Token not found in the response.")
    return None


bucketId = get_token(url2, api_token)
print("bucketId =", bucketId)
#bucketId = '''


'''
headers = {
  "Authorization": 'token',
  "Content-Type": 'application/json'
}'''
'''
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print(response.json())  # or response.text if not JSON
else:
    print(f"Failed to get access token: {response.status_code}")'''