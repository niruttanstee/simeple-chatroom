import socket
import threading

# get the hostname
host = "0.0.0.0"
port = 21004

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(10)
clients = [] # client objects
aliases = []

def broadcast(message):
    print(message.decode())
    for client in clients:
        client.send(message)
    
def handle_client(client):
    try:
        while True:
            message = client.recv(1024).decode()
            if not message:
                index = clients.index(client)
                alias = aliases[index]
                print(f"{alias} disconnected")
                clients.remove(client)
                aliases.remove(alias)
                client.close()
                break
            else:
                broadcast(message.encode())
    except:
        pass



def receive():
    while True:
        print('Server is running and listening...')
        client, address = server.accept()
        print(f'connection established with {str(address)}')
        client.send("alias?".encode())
        alias = client.recv(1024).decode()
        clients.append(client)
        aliases.append(alias)
        welcome_message = f"{str(alias)} has connected to the chat room\nthere are {len(clients)} user(s) in the chat room"
        broadcast(welcome_message.encode())
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()
        
if __name__ == "__main__":
    receive()