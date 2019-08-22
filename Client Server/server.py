import socket                
  
s = socket.socket()          
print ("Socket successfully created")

port = 12345                
  
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
  
s.listen(5)      
print ("socket is listening")            
  
while True: 

    c, addr = s.accept()    
    print ('Got connection from', addr) 
    output = input ("Enter Message :")

    c.sendall(output.encode('utf-8')) 

    #print (s.recv(1024)) 
   
c.close() 