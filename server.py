import socket 

class Server:
    port = 9500

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.socket.bind((self.host, Server.port))

    def _sendMessage(self, conn, message):
        conn.send(message.encode())
    
    def listen(self, printMesage=True):
        self.socket.listen()
        if printMesage:
            print('Server is Listening new Connection on Port : ', Server.port)
        self._acceptConnecton()

    def _acceptConnecton(self):
        print("server to accept connection")
        conn, addr = self.socket.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if data == b'Hello':
                    self._sendMessage(conn, 'Hi')
                else:
                    self._sendMessage(conn, 'Goodbye')
                    self.listen(False)

 
if __name__ == "__main__":
    server1 = Server()
    server1.listen()

