__author__ = "Ricardo Acosta"

import requests
from data import data

response = requests.get(data.REST_BASE_URL)

print("RESPONSE COOKIES")
for key, value in response.cookies.items():
    print("Cookie " + key, ": ", value)

