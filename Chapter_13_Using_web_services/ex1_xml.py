"""Exercise 1.

Change either geojson.py or geoxml.py to print out the
two-character country code from the retrieved data. Add
error checking so your program does not traceback if the
country code is not there. Once you have it working,
search for “Atlantic Ocean” and make sure it can handle
locations that are not in any country.
"""

import ssl
import urllib.error
import urllib.parse
import urllib.request

import defusedxml.ElementTree as ET  # pylint: disable=E0401

# import xml.etree.ElementTree as ET # !UNSAFE


API_KEY = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if API_KEY is False:
    API_KEY = 42
    SERVICE_URL = "http://py4e-data.dr-chuck.net/xml?"
else:
    SERVICE_URL = "https://maps.googleapis.com/maps/api/geocode/xml?"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break

    parameters = {}
    parameters["address"] = address
    if API_KEY is not False:
        parameters["key"] = API_KEY
    URL = SERVICE_URL + urllib.parse.urlencode(parameters)
    print("Retrieving", URL)

    # pylint: disable=R1732
    uh = urllib.request.urlopen(URL, context=ctx)  # nosec
    # pylint: enable=R1732

    data = uh.read()
    print("Retrieved", len(data), "characters")
    # print(data.decode())
    tree = ET.fromstring(data)

    lst = tree.findall("result/address_component")
    # print(lst)
    for item in lst:
        # print(item.find("short_name").text)
        if item.find("type").text == "country":
            country_code = item.find("short_name").text
            print(country_code)
            break
    else:
        print("No country code available")
