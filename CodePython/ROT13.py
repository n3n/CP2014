message = list(raw_input())
#n = input()
for i in range(len(message)):
	code = ord(message[i])
	if ord('a') <= code <= ord('z'):
		code = ord('a') + (code - ord('a') + 13) % 26
	elif ord('A') <= code <= ord('Z'):
		code = ord('A') + (code - ord('A') + 13) % 26
	message[i] = chr(code)
print ''.join(message)
