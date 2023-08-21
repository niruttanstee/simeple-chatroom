'''Socket programming in Python with client and server interaction'''
# Server is a listener socket
# Client reaches to the server
import socket
import sys
# AF_INET = IPV4 Address family, protocol of the internet
# SOCK_STREAM = connection protocol i.e. TCP, transmission control protocol

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket succesfully created!')
except socket.error as err:
    print(f'socket creation failed with error {err}')
    
port = 80

try:
    host_ip = socket.gethostbyname('www.nirutt.dev')
except socket.gaierror: # problem with DNS
    print('error resolving the host')
    sys.exit()

s.connect((host_ip, port))
print(f'socket has succesfully connected to Nirutt.dev on port == {host_ip}')