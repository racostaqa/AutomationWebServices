__author__ = "Ricardo Acosta"

import requests
from data import data

response_1 = requests.get(data.BASE_URL+'/users')  # Good request
response_2 = requests.get(data.BASE_URL+'/found/users')  # Bad request
print("STATUS CODES")
print("Status Code for Good Request: " + str(response_1.status_code))
print("Status Code for Bad Request: " + str(response_2.status_code))
