import requests
from datetime import datetime, timezone
from token_api import api_token
from bucketId import bucket_id

username = 'dxxxxxxxxt'
password = 'Fxxxxxxxxxx6'

headers = {
  'access-token': api_token
  }

files = [
    "ICRCounterparty_new.csv",
    "ICRInstrument_new.csv",
    "ICRCounterpartyInstrument_new.csv",
    "ICRFinancial_new.csv"
]

#removeafter
#bucket_id = 'aW5nZXN0aW9uX0ItRmluZV9kYXRhLWF1dG9tYXRpb25fMjAyNDEyMDZfbG90MDQ='
def get_signed_url(username, password, bucket_id, filename, headers):
    #url = f"https://xxxxxxxxxx={bucket_id}&filename={filename}"
    url = f"https://xxxxxxxxxxbucketId={bucket_id}&filename={filename}"
    return url
# List to store the signed URLs (response.text)

def save_signed_urls(files):
  signed_urls = []
  # Loop through each file to get the signed URL
  for file_name in files:
      try:
          getLinks = get_signed_url(username, password, bucket_id, file_name, headers)
          response = requests.get(getLinks, headers=headers, auth=(username, password))
          if response.status_code == 200:
              signed_url = response.json()
              #signedURL = signed_url['signedUrl']
              extracted_url = signed_url['signedUrl']
              signed_urls.append(extracted_url)  # Save the signed URL in the list
              #print(f"Response success for {file_name}! and its signed_url is {extracted_url}")
              #print("signedUrl==", signed_url)
          else:
              print(f"Failed for {file_name}. Status code:", response.status_code)
              print("Response content:", response.text)
      except requests.exceptions.RequestException as e:
          print(f"Request failed for {file_name}. Error: {e}")
  # Return only the valid signed URLs
  return signed_urls


signedUrl = save_signed_urls(files)
#print("urls are", signedUrl)



# Now you have a list of signed URLs that you can use later in the code
#print("signed URLs for {signed_url[2]}:", signed_urls[2])


#working  
#url = f"hxxxxx.csv"
'''
files = [
    "ICRCounterparty_new.csv"
]
response = requests.get(url, headers=headers, auth=(username, password))
if response.status_code == 200:
    get_file_link = response.json()
    print("link=", get_file_link)
else:
  print("link not found", response.json())'''