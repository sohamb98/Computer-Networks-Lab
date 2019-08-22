import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="localhost"
port =8000
s.connect((host,port))



while 2:
   data=s.recv(1024).decode()
   print("Received --> "+data)
   str="Acknowledgement: Message Received"
   #time.sleep(1.0)
   s.send(str.encode())

s.close ()