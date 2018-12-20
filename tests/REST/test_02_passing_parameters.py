__author__ = "Ricardo Acosta"

import requests
from data import data

parameters = {'page': '2'}
response = requests.get(data.REST_BASE_URL + '/users', params=parameters)
print(response.url)
print("\nGET REQUEST WITH PARAMETERS")
print(response.json())
