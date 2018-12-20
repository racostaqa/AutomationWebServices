__author__ = "Ricardo Acosta"

import requests
from data import data

response = requests.get(data.REST_BASE_URL + '/users')

print("RESPONSE HEADERS")
for key, value in response.headers.items():
    print(key, ": ", value)
