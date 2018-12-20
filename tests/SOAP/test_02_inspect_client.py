__author__ = "Ricardo Acosta"

from suds.client import Client
from data import data

client = Client(data.SOAP_URL)
print(client)

