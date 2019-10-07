import sys
import socket
import os
from socket import *
from lib import Lib
from PIL import Image

servername = '10.0.0.1'
PORT = 9000
BUFSIZE = 1000

def main(argv):
	clientSocket = socket(AF_INET,SOCK_STREAM) #TCP connection
        clientSocket.connect((servername,PORT))
        sti = raw_input('Indtast sti til fil:') 
        Lib.writeTextTCP(sti,clientSocket)
        
        f = open("receivedFile.png","w")
        size = int(Lib.readTextTCP(clientSocket))
        while size >1000:
            receive = clientSocket.recv(1000)
            f.write(receive)
            size = size-1000
           
        receive = clientSocket.recv(1000)
        try:
            f.write(receive)
        except:
            print("couldn't write the last part of the received file ")
            f.close()
            clientSocket.close()
        
        f.close()
        clientSocket.close()
        

    
if __name__ == "__main__":
   main(sys.argv[1:])
