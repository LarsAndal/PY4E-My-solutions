"""Exercise 3.

Use urllib to replicate the previous exercise of (1) retrieving
the document from a URL, (2) displaying up to 3000 characters, and
(3) counting the overall number of characters in the document. Don't
worry about the headers for this exercise, simply show the first 3000
characters of the document contents.
"""

from urllib.request import urlopen

url_input = input("Enter URL: ").lower()

try:
    if not url_input.startswith("http"):
        raise ValueError
    html = urlopen(url_input).read()  # nosec (fixed) , pylint: disable=R1732
    text = html.decode()
    print(text[:3000])
    print(len(text))
except (NameError, ValueError):
    print("Invalid URL")
