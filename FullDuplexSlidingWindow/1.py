import threading
import socket
import time

message = ['S','O','H','A','M','B','H','A','T','T','A','C','H','A','R','Y']
ack = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

def sender(c,start,end):
    for x in range(start,end):
        c.send(message[x].encode())
def checker(c,start,end):
    for x in range(start,end):
        if ack[x] != True:
            return x
    return -1

def send():
    time.sleep(2)
    s = socket.socket()          
    print ("Socket successfully created")

    port = 12345

    s.bind(('', port))         
    print ("socket binded to" + str(port)) 

    s.listen(5)      
    print ("socket is listening")

    window = 0
    start = -4
    ch = -1

    while True: 
        c, addr = s.accept()      
        print ('Got connection from'+str(addr))

        while(all(ack)!=True):
            if(ch!=-1):
                start = ch
                ch = -1
            else:
                start = start + 4
                window = window +4

            sender(c,start,window)

            for x in range(start,window):
                try:
                    index = c.recv(8).decode()
                    ack[int(index)] = True
                except socket.timeout:
                    print("Timed out!")
                    #going back
                    start  = x - 4
                    window = window - 4


            ch = checker(c,start,window)
        print(ch)
    
   
        c.close() 
        break

def recv():
    time.sleep(2)
    s = socket.socket()          
   
    port = 12346                

    #message = []
    s.connect(('127.0.0.1', port))
    #window = 4

    i = 0
    while(1):
        data=s.recv(1).decode()
        print("Received --> "+data)
        s.send(str(i).encode())
        i=i+1
    s.close()        


if __name__ == "__main__":
    t1 = threading.Thread(target=send) 
    t2 = threading.Thread(target=recv)
    t1.start()
    t2.start()

    t1.join()
    t2.join()