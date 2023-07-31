"""Exercise 4.

Change the urllinks.py program to extract and count paragraph
(p) tags from the retrieved HTML document and display the count
of the paragraphs as the output of your program. Do not display
the paragraph text, only count them. Test your program on several
small web pages as well as some larger web pages.
"""

import ssl
import urllib.error
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup  # pylint: disable=E0401

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Audit url open
url = input("Enter - ").lower()
if not url.startswith("http"):
    print("Invalid URL")
    exit()  # pylint: disable=R1722

# pylint: disable=R1732
html = urllib.request.urlopen(url, context=ctx).read()  # nosec (fixed)
# pylint: enable=R1732

soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the paragraph tags
tags = soup("p")
count = 0  # pylint: disable=C0103
for tag in tags:  # noqa
    count += 1
print(count)
