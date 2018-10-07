import requests
import json
from pprint import pprint

url = "https://gateway-staging.ncrcloud.com/catalog/items/snapshot"

headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'nep-application-key': "8a0287d86613f802016646e9bcb50015",
    'nep-organization': "ncr-market",
    'nep-service-version': "2.2.1:2",
    'Authorization': "Basic YWNjdDpoYWNrdGludGluQGhhY2t0aW50aW5zZXJ2aWNldXNlcjpXZWxjb21lMTIzIQ==",
    'Cache-Control': "no-cache",
    'Postman-Token': "69b0ad20-d6da-4771-9824-3838ccb4b8d0"
    }

response = requests.request("GET", url, headers=headers)
json_data = json.loads(response.text)

# print(response.text)
# pprint(json_data)

with open('data2.json', 'w') as fp:
    json.dump(pprint(json_data), fp)
