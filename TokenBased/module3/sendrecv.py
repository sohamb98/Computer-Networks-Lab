import threading
import socket
import time
import hashlib
import json
from queue import Queue 

token = "Token"
message = "Soham"

src = 12345
dest = 12346

checksum = hashlib.md5(message.encode()) 

frame = {
    'd': dest,
    's': src,
    'mess':message,
    'check': str(checksum)
}

finalframe = json.dumps(frame)

def send(out_q):
    time.sleep(2)
    
    s = socket.socket()          
    print ("Socket successfully created")

    port = 12346

    s.bind(('', port))         
    print ("socket binded to" + str(port)) 

    s.listen(5)      
    print ("socket is listening")

    while True: 
        c, addr = s.accept()      
        print ('Got connection from'+str(addr))
        c.send(message.encode())
        data=c.recv(1024).decode()
        out_q.put(data) 
        c.close() 
        break

def recv(out_q):
    time.sleep(2)
    s = socket.socket()          
   
    port = 12345

    data = out_q.get()
    
    while(data != token):
        data = out_q.get()

    if data == token:               
        s.connect(('127.0.0.1', port))

    while(1):

        data=s.recv(1024).decode()
        print(data)
        s.send(token.encode())
        break

    s.close()         


if __name__ == "__main__":
    q = Queue()

    t1 = threading.Thread(target=send,args =(q, )) 
    t2 = threading.Thread(target=recv,args =(q, ))
    t1.start()
    t2.start()

    t1.join()
    t2.join()