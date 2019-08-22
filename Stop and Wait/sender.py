import socket
import time
from threading import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket timeout
#serversocket.settimeout(0.5)


host = "localhost"
port = 8000

serversocket.bind((host,port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()
    def run(self):
        while 1:
            r=input("Send data -->")
            clientsocket.send(r.encode())
            acknowledged = False
            while not acknowledged:
                try:
                    print(clientsocket.recv(1024).decode())
                    acknowledged = True
                except socket.timeout:
                    print("Timed out trying Again")
                    clientsocket.send(r.encode())

serversocket.listen(5)
print ('Sender ready and is listening')
while (True):
    clientsocket, address = serversocket.accept()
    clientsocket.settimeout(0.5)
    print("Receiver "+str(address)+" connected")
    client(clientsocket, address)
