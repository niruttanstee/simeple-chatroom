import socket
import threading
import sys


alias = input("Enter alias: ")
host = "127.0.0.1"
port = 21004

client_socket = socket.socket()
client_socket.connect((host, port))

ask_alias = client_socket.recv(1024).decode()
if ask_alias == "alias?":
    client_socket.send(alias.encode())
else:
    client_socket.close()

def broadcast():
    while True:
        data = client_socket.recv(1024).decode()
        print(f"{data}")
        if not data:
            client_socket.close()
            
def send():
    while True:
        message = input("")
        if message == "quit":
            sys.exit()
        prefix = alias + ": " + message
        client_socket.send(prefix.encode())

if __name__ == '__main__':
    threading.Thread(target = send).start()
    threading.Thread(target = broadcast).start()

