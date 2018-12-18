__author__ = "Ricardo Acosta"

import requests
import json
from data import data

response = requests.delete('https://httpbin.org/delete')
response = requests.head('https://httpbin.org/get')
response = requests.options('https://httpbin.org/get')
