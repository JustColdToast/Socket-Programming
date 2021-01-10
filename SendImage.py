import socket


def formatdata(msg):  # This functions handles the formatting of a string of data for communication
    # Formatted messages should look as so: 0005>Hello  (The 0005 indicates that 5 bytes of data are being sent)
    bytecount = str(len(msg)+1)
    if len(bytecount) < 4:
        for i in range(0, 4-len(bytecount)):  # Adds 0's to the beginning of the number so that it is 4 digits
            bytecount = "0"+bytecount
    return bytecount+">"+msg

def sendImg(imgSrc):
    # Formatted messages should look as so: 0005>Hello  (The 0005 indicates that 5 bytes of data are being sent)
    with open(imgSrc, "rb") as f:
        data = f.read()
        b = bytearray(data)
    bytecount = str(len(b) + 1)
    if len(bytecount) < 4:
        for i in range(0, 4 - len(bytecount)):  # Adds 0's to the beginning of the number so that it is 4 digits
            bytecount = "0" + bytecount
    print(b)
    return bytecount + "i" + str(b)


sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sender.connect(('localhost', 4500))
sender.sendall(sendImg("img.jpg").encode())
