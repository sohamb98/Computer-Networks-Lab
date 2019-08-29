import socket 

s = socket.socket()          
   
port = 12345                

message = []
s.connect(('127.0.0.1', port))
window = 4

i = 0
while(1):
    data=s.recv(1).decode()
    print("Received --> "+data)
    s.send(str(i).encode())
    i=i+1
s.close()        
