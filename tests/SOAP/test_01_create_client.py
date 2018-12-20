__author__ = "Ricardo Acosta"

from suds.client import Client

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
client = Client(url)
