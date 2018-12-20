__author__ = "Ricardo Acosta"

import requests
from data import data

response = requests.delete(data.REST_BASE_URL + '/users/571')
print(response.url)
print("DELETE REQUEST")
print(response.status_code)
