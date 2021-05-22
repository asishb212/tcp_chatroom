import socket
import threading
import rospy
from nav_msgs.msg import Odometry
import time

local_host='127.0.0.1'
port=55555
global odom
odom=""
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
        #msg=f'{uname} : {input("")}'
        client.send(odom.encode('ascii'))

def bob(msg):
    print('gg')
    odom=msg
def ros_start():
    rospy.Subscriber("/odom",Odometry,bob)
rospy.init_node("ffff")
recieve_thread=threading.Thread(target=recieve)
recieve_thread.start()
write_thread=threading.Thread(target=write)
write_thread.start()
ros_thread=threading.Thread(target=ros_start)
ros_thread.start()

