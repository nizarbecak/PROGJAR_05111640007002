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

try:
    print('connected')
    # Recieve data
    file = open('ClientFile.txt','wb')
    while True:
        # Receive data and write it to file
        data = sock.recv(1024)
        if data:
            file.write(data)
            data = sock.recv(1024)
            file.close()
            print('saved to ClientFile.txt')
        else:
            break

finally:
    print('connection closed')
    sock.close()