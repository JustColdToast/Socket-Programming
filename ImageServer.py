import os
import io
from PIL import Image
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 4500))
server.listen(5)
while True:
    (client, address) = server.accept()
    print("New connection received from: " + str(address))
    imgData = client.recv(4096)
    img = Image.open(io.BytesIO(imgData))
    img.save("new.jpg")
