from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('192.168.43.191', serverPort))
print("The server is ready to recieve")
isChat = True
while isChat:
    message,clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode()
    print(modifiedMessage)
    replies = input('type your replies ')
    replyMsg = replies
    serverSocket.sendto(replyMsg.encode(), clientAddress)
    if replies == 'goodbye':
        isChat = False
serverSocket.close()
