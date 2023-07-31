"""Application 1.

Google geocoding web service, returns JSON.
"""

import json
import ssl
import urllib.error
import urllib.parse
import urllib.request

API_KEY = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if API_KEY is False:
    API_KEY = 42
    SERVICE_URL = "http://py4e-data.dr-chuck.net/json?"
else:
    SERVICE_URL = "https://maps.googleapis.com/maps/api/geocode/json?"

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

    # pylint: disable=C0103
    url = SERVICE_URL + urllib.parse.urlencode(parameters)

    print("Retrieving", url)
    # pylint: disable=R1732
    uh = urllib.request.urlopen(url, context=ctx)  # nosec
    # pylint: enable=R1732
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:  # noqa, pylint: disable=W0702
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("==== Failure To Retrieve ====")
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("lat", lat, "lng", lng)
    location = js["results"][0]["formatted_address"]
    print(location)
