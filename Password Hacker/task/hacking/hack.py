import socket
import sys
import string
import itertools


symbols = string.ascii_lowercase + string.digits
args = sys.argv
ip_address = args[1]
port = int(args[2])

with socket.socket() as client_socket:
    address = (ip_address, port)
    client_socket.connect(address)
    n = 1
    while True:
        for p in itertools.product(symbols, repeat=n):
            assert len(p) > 0
            password = ''.join(list(p))
            data = password.encode()
            client_socket.send(data)
            response = client_socket.recv(1024)
            response = response.decode()
            if response == 'Wrong password!':
                continue
            elif response == 'Connection success!':
                print(password)
                exit()
            elif response == "Too many attempts":
                exit()
        n += 1
