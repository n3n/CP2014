message = raw_input().split()
for i in message:
	if i == ' ':
		message.pop(message.index(i))

print ' '.join(message[::-1])

#print ' '.join(raw_input().split()[::-1])
