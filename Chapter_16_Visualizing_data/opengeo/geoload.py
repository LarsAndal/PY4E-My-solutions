"""Example from the book.

Load URLs from 'where.data' and look up coordinates to store in 'opengeo.sqlite'.
"""

import http
import json
import sqlite3
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request

SERVICE_URL = "https://py4e-data.dr-chuck.net/opengeo?"

# Additional detail for urllib
http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect("opengeo.sqlite")
cur = conn.cursor()

cur.execute(
    """
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)"""
)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data", encoding="utf-8")  # pylint: disable=R1732
count = 0  # pylint: disable=C0103
nofound = 0  # pylint: disable=C0103
for line in fh:
    if count > 100:
        print("Retrieved 100 locations, restart to retrieve more")
        break

    address = line.strip()
    print("")
    cur.execute(
        "SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()),),
    )

    try:
        data = cur.fetchone()[0]
        print("Found in database", address)
        continue
    except:  # nosec, pylint: disable=W0702
        pass

    parameters = {}
    parameters["q"] = address

    url = SERVICE_URL + urllib.parse.urlencode(parameters)  # pylint: disable=C0103

    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context=ctx)  # nosec, pylint: disable=R1732
    data = uh.read().decode()
    print("Retrieved", len(data), "characters", data[:20].replace("\n", " "))
    count = count + 1  # pylint: disable=C0103

    try:
        js = json.loads(data)
    except:  # nosec, pylint: disable=W0702
        print(data)  # We print in case unicode causes an error
        continue

    if not js or "features" not in js:
        print("==== Download error ===")
        print(data)
        break

    if len(js["features"]) == 0:
        print("==== Object not found ====")
        nofound = nofound + 1  # pylint: disable=C0103

    cur.execute(
        """INSERT INTO Locations (address, geodata)
                VALUES ( ?, ? )""",
        (memoryview(address.encode()), memoryview(data.encode())),
    )
    conn.commit()

    if count % 10 == 0:
        print("Pausing for a bit...")
        time.sleep(5)

if nofound > 0:
    print("Number of features for which the location could not be found:", nofound)

print(
    "Run geodump.py to read the data from the database so you can visualize it on a map."
)
