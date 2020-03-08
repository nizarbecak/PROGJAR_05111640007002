import socket
import sys

sock = socket.socket()
server_address = ('127.0.0.1', 31000) # Server 1
# server_address = ('127.0.0.1', 31001) # Server 2
# server_address = ('127.0.0.1', 31002) # Server 3
sock.bind(server_address)
sock.listen(1)
print(f"server with ip {server_address} is ON")

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    print(f"get a connection from {client_address}")

    # File to transfer
    file = open('ServerFile.txt', 'rb')

    # Send data
    message = file.read(1024)
    print(f"sending {message} from ServerFile.txt")
    while message:
        connection.send(message)
        message = file.read(1024)
    file.close()

    # Clean up the connection
    connection.close()
    print('client has been disconnected')