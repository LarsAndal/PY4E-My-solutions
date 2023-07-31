"""Exercise 2.

Change your socket program so that it counts the number of
characters it has received and stops displaying any text after it
has shown 3000 characters. The program should retrieve the entire
document and count the total number of characters and display
the count of the number of characters at the end of the document.
"""

import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

url_input = input("Enter URL: ")
url_list = url_input.split("/")

# Connect to host
try:
    host_name = url_list[2]
    my_socket.connect((host_name, 80))
    command = f"GET {url_input} HTTP/1.0\r\n\r\n".encode()
    my_socket.send(command)
except BaseException:  # pylint: disable=W0703
    print(f"Host unreachable: {url_input}")
    exit()  # pylint: disable=R1722

# Read text from host
text_raw = b""  # pylint: disable=C0103
while True:
    data = my_socket.recv(500)
    text_raw += data
    if len(data) < 1:
        break
# print(f"\nDebug: {data}\n")
# print(f"\nDebug: {text_raw}\n")

my_socket.close()

# Look for the end of the header
pos = text_raw.find(b"\r\n\r\n") + 4
# print(f"\nDebug: {text_raw[pos:].decode()}\n")

# Print 3000 characters and display number of characters
text = text_raw[pos:].decode()
print(text[:3000])
print(len(text))
