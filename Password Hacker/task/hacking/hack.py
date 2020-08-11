import socket
import sys


args = sys.argv
ip_address = args[1]
port = int(args[2])
message = args[3]

with socket.socket() as client_socket:
    address = (ip_address, port)
    client_socket.connect(address)

    data = message.encode()
    client_socket.send(data)

    response = client_socket.recv(1024)
    response = response.decode()
    print(response)
ping