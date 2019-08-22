import socket

UDP_IP_ADDRESS = "192.168.41.38"
UDP_PORT_NO = 1234
Message = "Soham 116cs0171"
Message = Message.encode('utf-8')

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))


