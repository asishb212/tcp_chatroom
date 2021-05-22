import socket
import threading
import os
from pyngrok import ngrok

host='127.0.0.1'
port=55555

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind a local socket to the port
server_address = ("", port)
sock.bind(server_address)
sock.listen(1)

# Open a ngrok tunnel to the socket
public_url = ngrok.connect(port, "tcp", options={"remote_addr": "{}:{}".format(host, port)})
print("ngrok tunnel \"{}\" -> \"tcp://127.0.0.1:{}/\"".format(public_url, port))

clients=[]
unames=[]

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            idx=clients.index(client)
            clients.remove(client)
            clients.close()
            broadcast(f'{unames[idx]} left the chat!'.encode('ascii'))
            unames.remove(unames[idx])
            break

def recieve_handler():
    while True:
        client,address=sevrer.accept()
        print(f"connected : {str(address)}")
        client.send("initalmsg".encode('ascii'))
        uname=client.recv(1024).decode('ascii')
        unames.append(uname)
        clients.append(client)
        print(f'{uname} connected')
        broadcast(f"{uname} joined".encode('ascii'))
        client.send("connected to server".encode('ascii'))

        thread=threading.Thread(target=handle_client,args=(client,))
        thread.start()

recieve_handler()

