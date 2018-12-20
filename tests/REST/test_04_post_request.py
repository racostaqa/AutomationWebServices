__author__ = "Ricardo Acosta"

import requests
import json
from data import data

user = {'name': 'Ricardo', 'job': 'QA Tester'}
response = requests.post(data.REST_BASE_URL + '/users', data=user)
print(response.url)
print("POST REQUEST")
print(json.dumps(response.json(), indent=4))
