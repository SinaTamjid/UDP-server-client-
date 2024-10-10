from socket import *
#local server name
serverName = '127.0.0.1'
# it can be any server port just make sure your giving the same value in UDP_server
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
#get the massage you trying to pass to the server
message = input(r'inpute lowercase letters:')
clientSocket.sendto(message.encode(),( serverName,serverPort,))
modifiedMessage,severaddress=clientSocket.recvfrom(2048)
#making sure that the massage send and printing  it
print(modifiedMessage)
#we make sure that after sending massage we close the socket
clientSocket.close()


