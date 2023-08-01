"""Example from the book.

The first step is to spider the repository. The base URL
is hard-coded in the gmane.py and is hard-coded to the Sakai
developer list. Make sure to delete the content.sqlite file if you
switch the base url. The gmane.py file operates as a spider in
that it runs slowly and retrieves one mail message per second so
as to avoid getting throttled by gmane.org.   It stores all of
its data in a database and can be interrupted and re-started
as often as needed. It may take many hours to pull all the data
down.  So you may need to restart several times.

The second process is running the program gmodel.py. gmodel.py reads the rough/raw
data from content.sqlite and produces a cleaned-up and well-modeled version of the
data in the file index.sqlite.  The file index.sqlite will be much smaller (often 10X
smaller) than content.sqlite because it also compresses the header and body text.
"""

import re
import sqlite3
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta
from urllib.parse import urljoin, urlparse

# Not all systems have this so conditionally define parser
try:
    import dateutil.parser as parser
except:
    pass


def parsemaildate(md):  # pylint: disable=C0103
    """See if we have dateutil."""
    try:
        pdate = parser.parse(tdate)
        test_at = pdate.isoformat()
        return test_at
    except:
        pass

    # Non-dateutil version - we try our best

    pieces = md.split()
    notz = " ".join(pieces[:4]).strip()

    # Try a bunch of format variations - strptime() is *lame*
    dnotz = None
    for form in [
        "%d %b %Y %H:%M:%S",
        "%d %b %Y %H:%M:%S",
        "%d %b %Y %H:%M",
        "%d %b %Y %H:%M",
        "%d %b %y %H:%M:%S",
        "%d %b %y %H:%M:%S",
        "%d %b %y %H:%M",
        "%d %b %y %H:%M",
    ]:
        try:
            dnotz = datetime.strptime(notz, form)
            break
        except:
            continue

    if dnotz is None:
        # print 'Bad Date:',md
        return None

    iso = dnotz.isoformat()

    tz = "+0000"  # pylint: disable=C0103
    try:
        tz = pieces[4]  # pylint: disable=C0103
        # ival = int(tz)  # Only want numeric timezone values
        if tz == "-0000":
            tz = "+0000"  # pylint: disable=C0103
        tzh = tz[:3]
        tzm = tz[3:]
        tz = tzh + ":" + tzm  # pylint: disable=C0103
    except:
        pass

    return iso + tz


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect("content.sqlite")
cur = conn.cursor()

baseurl = "http://mbox.dr-chuck.net/sakai.devel/"  # pylint: disable=C0103

cur.execute(
    """CREATE TABLE IF NOT EXISTS Messages
    (id INTEGER UNIQUE, email TEXT, sent_at TEXT,
     subject TEXT, headers TEXT, body TEXT)"""
)

# Pick up where we left off
start = None  # pylint: disable=C0103
cur.execute("SELECT max(id) FROM Messages")
try:
    row = cur.fetchone()
    if row is None:
        start = 0  # pylint: disable=C0103
    else:
        start = row[0]
except:
    start = 0  # pylint: disable=C0103

if start is None:
    start = 0  # pylint: disable=C0103

many = 0  # pylint: disable=C0103
count = 0  # pylint: disable=C0103
fail = 0  # pylint: disable=C0103
while True:
    if many < 1:
        conn.commit()
        sval = input("How many messages:")
        if len(sval) < 1:
            break
        many = int(sval)

    start = start + 1
    cur.execute("SELECT id FROM Messages WHERE id=?", (start,))
    try:
        row = cur.fetchone()
        if row is not None:
            continue
    except:
        row = None  # pylint: disable=C0103

    many = many - 1
    url = baseurl + str(start) + "/" + str(start + 1)  # pylint: disable=C0103

    text = "None"  # pylint: disable=C0103
    try:
        # Open with a timeout of 30 seconds
        document = urllib.request.urlopen(url, None, 30, context=ctx)
        text = document.read().decode()
        if document.getcode() != 200:
            print("Error code=", document.getcode(), url)
            break
    except KeyboardInterrupt:
        print("")
        print("Program interrupted by user...")
        break
    except Exception as e:
        print("Unable to retrieve or parse page", url)
        print("Error", e)
        fail = fail + 1  # pylint: disable=C0103
        if fail > 5:
            break
        continue

    print(url, len(text))
    count = count + 1  # pylint: disable=C0103

    if not text.startswith("From "):
        print(text)
        print("Did not find From ")
        fail = fail + 1  # pylint: disable=C0103
        if fail > 5:
            break
        continue

    pos = text.find("\n\n")
    if pos > 0:
        hdr = text[:pos]
        body = text[pos + 2 :]
    else:
        print(text)
        print("Could not find break between headers and body")
        fail = fail + 1  # pylint: disable=C0103
        if fail > 5:
            break
        continue

    email = None  # pylint: disable=C0103
    x = re.findall("\nFrom: .* <(\S+@\S+)>\n", hdr)  # pylint: disable=W1401
    if len(x) == 1:
        email = x[0]
        email = email.strip().lower()
        email = email.replace("<", "")
    else:
        x = re.findall("\nFrom: (\S+@\S+)\n", hdr)  # pylint: disable=W1401
        if len(x) == 1:
            email = x[0]
            email = email.strip().lower()
            email = email.replace("<", "")

    date = None  # pylint: disable=C0103
    y = re.findall("\Date: .*, (.*)\n", hdr)  # pylint: disable=W1401
    if len(y) == 1:
        tdate = y[0]
        tdate = tdate[:26]
        try:
            sent_at = parsemaildate(tdate)
        except:
            print(text)
            print("Parse fail", tdate)
            fail = fail + 1  # pylint: disable=C0103
            if fail > 5:
                break
            continue

    subject = None  # pylint: disable=C0103
    z = re.findall("\Subject: (.*)\n", hdr)  # pylint: disable=W1401
    if len(z) == 1:
        subject = z[0].strip().lower()

    # Reset the fail counter
    fail = 0  # pylint: disable=C0103
    print("   ", email, sent_at, subject)
    cur.execute(
        """INSERT OR IGNORE INTO Messages (id, email, sent_at, subject, headers, body)
        VALUES ( ?, ?, ?, ?, ?, ? )""",
        (start, email, sent_at, subject, hdr, body),
    )
    if count % 50 == 0:
        conn.commit()
    if count % 100 == 0:
        time.sleep(1)

conn.commit()
cur.close()
