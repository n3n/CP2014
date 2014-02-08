import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    c.send('What\'s your name ?')
    usr = c.recv(1024)
    print usr
    c.send('Thank you for connecting '+usr)
    c.close()
