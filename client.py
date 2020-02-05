import socket
import sys

from server import Server

class Client():
<<<<<<< HEAD
=======
 
>>>>>>> 1d898b8447809d1fe05751941a82eea13d7e74f4
    port = 9500
    
    def __init__(self):
        self.socket = socket.socket()
        self.host = socket.gethostname()
    
    def getConnection(self, host, port):
        self.socket.connect((self.host, port))
    
    def endConnection(self):
        self.socket.close()

    def recieveMessage(self):
       data = self.socket.recv(1024)
       return data.decode()


    def sendMessage(self, message):
        self.socket.sendall(message.encode())

if __name__ == "__main__":
     # message = "Hello" # this value is the message should be sent
    print("Input message to send :")
    message = sys.stdin.readline()[:-1]


    client = Client()
    print("Host:", client.host)
    print("Port:", Client.port)
    client.getConnection(client.host, Client.port)

    print("sending Message:", message)
    client.sendMessage(message)
    receiveMessage = client.recieveMessage()
    print("received Message :", receiveMessage)
 
 
