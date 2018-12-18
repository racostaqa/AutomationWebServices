__author__ = "Ricardo Acosta"

import requests
from data import data

response = requests.get(data.BASE_URL+'/users')

for key, value in response.headers.items():
    print(key, ": ", value)
