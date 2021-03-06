import socket
import threading
from sys import argv


text_colour_dict = {'green': '\033[0;32m', 'red':'\033[0;31m', 'yellow':'\033[0;33m', 
                    'light_cyan':'\033[96m', 'light_yellow':'\033[93m', 
                    'bright_magenta':'\033[1;35;40m'}


local_host = argv[1]
port = int(argv[2])
colour = argv[3] 

colour_chosen = text_colour_dict[colour]

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((local_host,port))
uname=input("Choose a username: ")

def recieve():
    while True:
        try:
            msg=client.recv(1024).decode('ascii')
            if msg=='Initalmsg':
                client.send(uname.encode('ascii'))
            else:
                print(msg)
        except:
            print("Connection failed")
            client.close()
            break

def write():
    while True:
        msg=f'%s{uname} : {input("")}%s' % (colour_chosen, '\033[0m')
        client.send(msg.encode('ascii'))

recieve_thread=threading.Thread(target=recieve)
recieve_thread.start()
write_thread=threading.Thread(target=write)
write_thread.start()

