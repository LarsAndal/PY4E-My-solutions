"""Example from the book.

Read data from 'opengeo.sqlite' and write the data to 'where.js'.
Makes it possible to open 'where.html' to display the locations.
"""

import codecs
import json
import sqlite3

conn = sqlite3.connect("opengeo.sqlite")
cur = conn.cursor()

cur.execute("SELECT * FROM Locations")
fhand = codecs.open("where.js", "w", "utf-8")  # pylint: disable=R1732
fhand.write("myData = [\n")
count = 0  # pylint: disable=C0103
for row in cur:
    data = str(row[1].decode())  # pylint: disable=C0103
    try:
        js = json.loads(str(data))
    except:  # nosec, pylint: disable=W0702
        continue

    if len(js["features"]) == 0:
        continue

    try:
        lat = js["features"][0]["geometry"]["coordinates"][1]
        lng = js["features"][0]["geometry"]["coordinates"][0]
        where = js["features"][0]["properties"]["display_name"]
        where = where.replace("'", "")
    except:  # nosec, pylint: disable=W0702
        print("Unexpected format")
        print(js)

    try:
        print(where, lat, lng)

        count = count + 1  # pylint: disable=C0103
        if count > 1:
            fhand.write(",\n")
        output = "[" + str(lat) + "," + str(lng) + ", '" + where + "']"
        fhand.write(output)
    except:  # nosec, pylint: disable=W0702
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")
