import socket
import threading

#local_host='127.0.0.1'
#port=55555
local_host='8.tcp.ngrok.io'
port=16171
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((local_host,port))
uname=input("choose a name")

def recieve():
    while True:
        try:
            msg=client.recv(1024).decode('ascii')
            if msg=='initalmsg':
                client.send(uname.encode('ascii'))
            else:
                print(msg)
        except:
            print("connection failed")
            client.close()
            break

def write():
    while True:
        msg=f'{uname} : {input("")}'
        client.send(msg.encode('ascii'))

recieve_thread=threading.Thread(target=recieve)
recieve_thread.start()
write_thread=threading.Thread(target=write)
write_thread.start()

