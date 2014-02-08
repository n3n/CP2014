import socket

s = socket.socket()
host = socket.gethostname()
port = 3889
s.bind((host, port))

s.listen(5)
while True:
    c, ad
