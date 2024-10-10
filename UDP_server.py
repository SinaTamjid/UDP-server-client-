from socket import *
# it can be any server port just make sure your giving the same value in UDP_client
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("The Server is ready to receive")
while True:
               message,clientAddress = serverSocket.recvfrom(2048)
               modifiedMessage =message.upper()
               serverSocket.sendto(modifiedMessage,clientAddress)

