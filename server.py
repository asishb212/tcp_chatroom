import socket
import threading
from pyngrok import ngrok


clients=[]
unames=[]


host = "1.tcp.ngrok.io"
port = 12345

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind a local socket to the port
server_address = ("", port)
sock.bind(server_address)
sock.listen(1)

# Open a ngrok tunnel to the socket
public_url = ngrok.connect(port, "tcp", options={"remote_addr": "{}:{}".format(host, port)})
a = public_url
a = str(a)


print("\nHOSTNAME =", a[20:34])
print("PORT =", a[35:40])



def broadcast(message):
    
    try:
        for client in clients:
            client.send(message)

    except:
        pass

def handle_client(client):
    while True:

        try:
            message=client.recv(1024)
            broadcast(message)

        except BrokenPipeError:

            idx=clients.index(client)
            clients.remove(client)
            broadcast(f'\033[0;31m{unames[idx]} left the chat!\033[0m'.encode('ascii'))
            unames.remove(unames[idx])

def recieve_handler():
    while True:
        client,address=sock.accept()
        print(f"\n\033[96m(Hostname, Port) : {str(address)}\033[0m")
        client.send("Initalmsg".encode('ascii'))
        uname=client.recv(1024).decode('ascii')
        unames.append(uname)
        clients.append(client)
        print(f'\033[1;32;40m{uname} Connected\033[0m')
        broadcast(f"\n\033[93m{uname} Joined\033[0m\n".encode('ascii'))
        client.send("\033[1;32;40mConnected to server\033[0m\n".encode('ascii'))

        thread=threading.Thread(target=handle_client,args=(client,))
        thread.start()

recieve_handler()

