"""Exercise 5.

(Advanced) Change the socket program so that it only shows data
after the headers and a blank line have been received. Remember
that recv receives characters (newlines and all), not lines.
"""

import socket

# Socket setup
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("data.pr4e.org", 80))
COMMAND = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
my_socket.send(COMMAND)

# Get page data
html = b""  # pylint: disable=C0103
while True:
    data = my_socket.recv(512)
    html += data
    if len(data) < 1:
        break
    # print(html.decode(), end="")
my_socket.close()

pos = html.find(b"\r\n\r\n") + 3
text = html[pos:].decode()
print(text)
