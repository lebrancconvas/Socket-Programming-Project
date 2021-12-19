import socket 

port = 12000
server = "192.168.1.132"

# Create Socket Object. 
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

message = input("Input: ")

clientSocket.sendto(message.encode(),(server, port))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(serverAddress, modifiedMessage.decode())  

clientSocket.close() 