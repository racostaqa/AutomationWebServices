__author__ = "Ricardo Acosta"

import requests
from data import data

response = requests.get(data.BASE_URL)

for key, value in response.cookies.items():
    print("Cookie " + key, ": ", value)

