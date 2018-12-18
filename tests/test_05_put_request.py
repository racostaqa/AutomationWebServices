__author__ = "Ricardo Acosta"

import requests
import json
from data import data

user = {'name': 'Ricardo Acosta', 'job': 'QA Tester Engineer'}
response = requests.put(data.BASE_URL+'/users/751', data=user)
print(response.url)
print("PUT REQUEST")
print(json.dumps(response.json(), indent=4))
