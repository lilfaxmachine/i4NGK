import sys
import os
from socket import *
from lib import Lib

PORT = 9000
BUFSIZE = 800
CHUNK_SIZE = 1000

def main(argv):
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('10.0.0.1',PORT))
    serverSocket.listen(1)
    #serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    print('Server klar til at modtage')
    while True:
        connectSocket, addr = serverSocket.accept()
        sti = Lib.readTextTCP(connectSocket)
        print(sti)
        
        try:
            f = open(sti, 'r+')
        except:
            print("An exception occurred. Can't open path.")
	try:
            tempSize = os.path.getsize(sti)
	except:
	    print("path or file is inaccessible")
        Lib.writeTextTCP(str(tempSize),connectSocket)
        with f as infile:
            while True:
                if tempSize>CHUNK_SIZE:
                    tempSize = tempSize-CHUNK_SIZE
                    chunk = infile.read(CHUNK_SIZE)
                    connectSocket.send(chunk)
                else:
                    chunk = infile.read(CHUNK_SIZE)
                    connectSocket.send(chunk)
                    break
        
        print("File is transmitted")
        connectSocket.close()
    

if __name__ == "__main__":
   main(sys.argv[1:])
