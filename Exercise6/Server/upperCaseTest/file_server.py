import sys
import socket
from socket import *
from lib import Lib

PORT = 9000
BUFSIZE = 1000


def main(argv):
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('10.0.0.1',PORT))
    serverSocket.listen(1)
    print('Server klar til at modtage')
    while True:
        connectSocket, addr = serverSocket.accept()
        sti = connectSocket.recv(BUFSIZE).decode()
        sti_med_stort = sti.upper()
        connectSocket.send(sti_med_stort.encode())
        connectSocket.close()
    

if __name__ == "__main__":
   main(sys.argv[1:])
