import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MASSAGE = "!DISCONNECT"
#SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "192.168.1.30"
ADDR = (SERVER, PORT)

#crate socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to server
client.connect(ADDR)

#function send massage to server
def send(msg):
    #encode massage to byte format
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
    #print massage receive from server
    print(client.recv(2048).decode(FORMAT))
    
send("Hello!")
input()
send("Ploy")
input()
send(DISCONNECT_MASSAGE)
 