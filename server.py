# Server has a bind method that binds to a specific IP and port to ensure
# consistent connection.

# methods: bind() binds address, listen() enables listening of client,
# accept() accepts connection, close() close connection

import socket
s = socket.socket()
print('socket succesfully created')
port = 56789
try:
    s.bind(('', port))
    print(f'socket binded to port: {port}')
except socket.error as err:
    print(f'socket cannot bind to port: {err}')

s.listen(5) # listen to a max of 5 connections.
print('socket is listening')
while True:
    c, addr = s.accept()
    print('got connection from', addr)
    message = ('Thank you for connecting\n')
    c.send(message.encode())
    c.close()