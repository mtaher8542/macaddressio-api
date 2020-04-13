import sys
import requests
from find_companyname import extract_values_from_json
import json


if len(sys.argv) == 2:
	arg=sys.argv[1]
else:
	print('Please enter only one MAC address')
	exit(0)	
#API Call to macaddress.io based on MAC address 
response = requests.get('https://api.macaddress.io/v1?apiKey=at_XqoZnDcHehod4A6dhlpTZgNIGoGnK&output=json&search='+arg)
if(response):
	#Calling the function to extract CompanyName
	companyname = extract_values_from_json(response.json(),'companyName')
	#Convert list to string in print statement
	print('CompanyName  : ' +' '.join(map(str, companyname)))
else:
	print("CompanyName Not Found")

