import requests
import json
import csv
from datetime import datetime, timezone
import os
import subprocess
from requests.auth import HTTPBasicAuth
from get_file_link_ICR import signedUrl
from token_api import api_token

username = 'xxxxxx'
password = 'xxx#xxxxxxx'

#print("urls[1]", signedUrl[1])
headers = {
  'access-token': api_token,
  #'Content-Type': 'multipart/form-data'
  }

files = {
    'dataAppFile1': ('ICRCounterparty_new.csv', open('ICRCounterparty_new.csv', 'rb'), 'text/csv'),
    'dataAppFile2': ('ICRInstrument_new.csv', open('ICRInstrument_new.csv', 'rb'), 'text/csv'),
    'dataAppFile3': ('ICRCounterpartyInstrument_new.csv', open('ICRCounterpartyInstrument_new.csv', 'rb'), 'text/csv'),
    'dataAppFile4': ('ICRFinancial_new.csv', open('ICRFinancial_new.csv', 'rb'), 'text/csv')
}

for url, (file_key, file_entry) in zip(signedUrl, files.items()):
    file_data = {file_key: file_entry}
    response = requests.put(url, headers=headers, files=file_data, auth=HTTPBasicAuth(username, password))
    if response.status_code == 200:
        print(f"Success for {file_key}:", response.json())
    else:
        print(f"Error for {file_key}:", response.status_code)
        print("Response Text:", response.text)

'''
for i, url in enumerate(signedUrl, start=1):
  file_key = f'dataAppFile{i}'
  file_entry = {file_key: files[file_key]}

  response = requests.put(url, headers=headers, files=file_entry, auth=HTTPBasicAuth(username, password))
  if response.status_code == 200:
      print(f"Success for {file_key}:", response.json())
  else:
      print(f"Error for {file_key}:", response.status_code)
      print("Response Text:", response.text)
'''

'''response = requests.put(url, headers=headers, files=files, auth=HTTPBasicAuth(username, password))
  if response.status_code == 200:
    print("success", response.json())
  else:
    print("error", response.status_code)
    print("Response Text:", response.text)
'''
#working as single file
'''
files = {
    'dataAppFile': ('ICRCounterparty_new.csv', open('ICRCounterparty_new.csv', 'rb'), 'text/csv')
}

url = "xxxxxxxx"

response = requests.put(url, headers=headers, files=files, auth=HTTPBasicAuth(username, password))
if response.status_code == 200:
  print("success", response.json())
else:
  print("error", response.status_code)
  print("Response Text:", response.text)'''