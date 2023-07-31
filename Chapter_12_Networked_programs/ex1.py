"""Exercise 1.

Change the socket program socket1.py to prompt the user for the
URL so it can read any web page. You can use split('/') to break
the URL into its component parts so you can extract the host name
for the socket connect call. Add error checking using try and
except to handle the condition where the user enters an improperly
formatted or non-existent URL
"""

import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# my_socket.connect(("data.pr4e.org", 80))

url_input = input("Enter URL: ")
url_list = url_input.split("/")

try:
    host_name = url_list[2]
    my_socket.connect((host_name, 80))
    # command = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
    command = f"GET {url_input} HTTP/1.0\r\n\r\n".encode()
    my_socket.send(command)
except BaseException:  # pylint: disable=W0703
    print(f"Host unreachable: {url_input}")
    exit()  # pylint: disable=R1722

while True:
    data = my_socket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")

my_socket.close()
