import socket


def formatdata(msg):  # This functions handles the formatting of a string of data for communication
    # Formatted messages should look as so: 0005>Hello  (The 0005 indicates that 5 bytes of data are being sent)
    bytecount = str(len(msg)+1)
    if len(bytecount) < 4:
        for i in range(0, 4-len(bytecount)):  # Adds 0's to the beginning of the number so that it is 4 digits
            bytecount = "0"+bytecount
    return bytecount+">"+msg


def sendMsg(msg):
    # Formatted messages should look as so: 0005>Hello  (The 0005 indicates that 5 bytes of data are being sent)
    bytecount = str(len(msg) + 1)
    if len(bytecount) < 4:
        for i in range(0, 4 - len(bytecount)):  # Adds 0's to the beginning of the number so that it is 4 digits
            bytecount = "0" + bytecount
    return bytecount + "m" + msg


def sendImg(imgSrc):
    # Formatted messages should look as so: 0005>Hello  (The 0005 indicates that 5 bytes of data are being sent)
    with open(imgSrc, "rb") as f:
        data = f.read()
        b = bytearray(data)
    bytecount = str(len(b) + 1)
    if len(bytecount) < 4:
        for i in range(0, 4 - len(bytecount)):  # Adds 0's to the beginning of the number so that it is 4 digits
            bytecount = "0" + bytecount
    return bytecount + "i" + str(b)


# Begin mainloop, asks for message, converts to bytes, and sets
while True:
    # Create the socket used for TCP connection
    sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to a pre-opened port on target IP
    print("------------\nConnecting.....")
    print("Connected\n------------")
    sender.connect(('localhost', 4500))
    # Sockets are destroyed after a single transmission, must be re-created each time

    # Below gets user input and tries to send data to server after formatting
    try:
        sender.sendall(str.encode(sendMsg(input("Enter your message: "))))
        print("-----\nSent\n-----")
    except:  # Yes, I'm using a broad except clauses; I believe in true exception equality
        print("Transmission failed")
