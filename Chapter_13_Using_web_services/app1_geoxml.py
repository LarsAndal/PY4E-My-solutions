"""Application 1.

Google geocoding web service, returns XML.
"""

import ssl
import urllib.error
import urllib.parse
import urllib.request

# trunk-ignore(pylint/E0401)
import defusedxml.ElementTree as ET

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
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall("result")
    lat = results[0].find("geometry").find("location").find("lat").text
    lng = results[0].find("geometry").find("location").find("lng").text
    location = results[0].find("formatted_address").text

    print("lat", lat, "lng", lng)
    print(location)
