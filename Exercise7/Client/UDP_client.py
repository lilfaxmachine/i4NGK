from socket import * 
serverName = '10.0.0.1'
serverPort = 9000
RECV_BUF = 10000

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Input a letter u to get the uptime status file or input the letter l for the loadavg file (CPU load):')
try:
    clientSocket.sendto(message,(serverName,serverPort))
except:
    print("Couldn't send message")
print(message)
file_from_server, serverAddress = clientSocket.recvfrom(RECV_BUF)
print(file_from_server)
clientSocket.close()
