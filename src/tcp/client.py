import socket

PORT = 12000
SERVER = socket.gethostbyname(socket.gethostname())

#create socket object
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((SERVER, PORT))

sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(2048)
print('From server:', modifiedSentence.decode())

clientSocket.close()
