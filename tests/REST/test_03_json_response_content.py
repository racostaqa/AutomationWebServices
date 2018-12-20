__author__ = "Ricardo Acosta"

import requests
import json
from data import data

response = requests.get(data.REST_BASE_URL + '/users')
print("GET REQUEST")
print(json.dumps(response.json(), indent=4))
