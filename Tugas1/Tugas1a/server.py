import socket
import sys

s = socket.socket()
server_address = ('127.0.0.1', 31000) # Server 1
# server_address = ('127.0.0.1', 31001) # Server 2
# server_address = ('127.0.0.1', 31002) # Server 3
s.bind(server_address)
s.listen(1)
print(f"server with ip {server_address} is ON")

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = s.accept()
    print(f"get a connection from {client_address}")

    # File to save the transferred message
    file = open('ServerFile.txt', 'wb')

    # Receive the data in small chunks and retransmit it
    while True:
        # receive data and write it to file
        data = connection.recv(1024)
        if data:
            file.write(data)
            data = connection.recv(1024)

            file.close()
            print('saved to ServerFile.txt')
        else:
            break

    # Clean up the connection
    connection.close()
    print('client has been disconnected')