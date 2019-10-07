import sys
from socket import *

serverPort = 9000
RECV_BUF = 10000

serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('10.0.0.1',serverPort))
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(RECV_BUF)
    if ((message == 'l') or (message == 'L')):
        try:
            f = open("../../../proc/loadavg","r")
            content = f.read()
        except:
            print("Couldn't open proc/loadavg")
        serverSocket.sendto(content,clientAddress)
    elif ((message == 'U') or (message == 'u')):
        try:
            f = open("../../../proc/uptime")
            content = f.read()
        except:
            print("Couldn't open proc/uptime")
        serverSocket.sendto(content,clientAddress)
    else:
        content = "Invalid letter or other fail"
        serverSocket.sendto(content,clientAddress)

            

