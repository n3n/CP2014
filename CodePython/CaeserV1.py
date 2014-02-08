n = input()
message = raw_input()
caesar = ''
for i in xrange(len(message)):
    code = ord(message[i])
    if 97 <= code <= 122:
    	caesar += chr( 97 + (code - 97 + n) % 26 )
    elif 65 <= code <= 90:
		caesar += chr( 65 + (code - 65 + n) % 26 )
    else:
		caesar += message[i]
print caesar