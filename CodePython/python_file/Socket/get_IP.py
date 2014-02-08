import socket

# Get Your IP address

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com', 0))
s.getsockname()[0]

