import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000) # Server 1
# server_address = ('localhost', 31001) # Server 2
# server_address = ('localhost', 31002) # Server 3
print(f"connecting to {server_address}")
sock.connect(server_address)

# File to transfer
file = open("ClientFile.txt", 'rb')

try:
    print('connected')

    # Send data
    message = file.read(1024)
    print(f"sending {message} from ClientFile.txt")
    while message:
        sock.send(message)
        message = file.read(1024)

    file.close()
finally:
    print('connection closed')
    sock.close()