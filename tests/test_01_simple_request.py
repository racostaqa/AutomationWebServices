__author__ = "Ricardo Acosta"

import requests
from data import data

response = requests.get(data.BASE_URL + '/users')
print("\nGET REQUEST")
print(response.json())
