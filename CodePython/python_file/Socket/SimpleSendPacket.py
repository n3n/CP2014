import socket
import sys

##################################################################

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = socket.gethostname()
bytes = '65500'
ip = socket.gethostbyname(socket.gethostname())
port = raw_input()

while True:
	s.sendto(bytes,(ip, port))
