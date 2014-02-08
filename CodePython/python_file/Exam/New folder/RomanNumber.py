number = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
value = 0
message = raw_input()
length = len(message)
for i in range(len(message)):
	if message[i] == message[-1]:
		value += number[message[i]]
	elif number[message[i]] < number[message[i+1]]:
		value += number[message[i]]*-1
	else:
		value += number[message[i]]
print value
