import os
import io
from PIL import Image
import socket
lastConnection = (0,)  # This tracks the last connection
# Setup socket for TCP connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to the localhost and target ip
server.bind(('localhost', 4500))

# Wait for incoming client requests, will accept a maximum of 5 before closing
print("Listening....")
server.listen(5)
while True:
    # The below assigns any inbound connections a client name and client address
    (client, address) = server.accept()
    if address[0] == lastConnection:
        print("Connection refreshed")
    else:
        print("New connection received from: " + str(address))
        print(address[0], lastConnection)
    lastConnection = address[0]
    # Below is the method of communication
    # First receives the number of bytes of data to be transmitted (must be decoded)
    # Second, receives that many bytes worth of data, prints it decoded
    identifier = client.recv(5).decode()
    if "m" in identifier:  # If a message is being transmitted
        print(client.recv(int(identifier[:4])).decode())
    elif "i" in identifier:  # If an image is being transmitted
        imgData = client.recv(int(identifier[:4])).decode()
        print(client.recv(int(identifier[:4])))
        img = Image.open(io.BytesIO(bytearray(imgData)))

