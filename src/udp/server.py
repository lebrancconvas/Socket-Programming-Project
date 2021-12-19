import socket 
port = 12000 
server = "192.168.1.132"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
serverSocket.bind((server, port)) 

print("UDP Server Up and Listening.") 

while(True): 
	bytesAddress = serverSocket.recvfrom(2048)
	