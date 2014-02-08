def encaesar(character,i):
	code = ord(character)
	if 97 <= code <= 122:
		code = 97 + (code - 97 + i) % 26
	elif 65 <= code <= 90:
		code = 65 + (code - 65 + i) % 26
	else:
		pass
	return chr(code)
#----------------------------------------__#
def decaesar(character,i):
	code = ord(character)
	if 97 <= code <= 122:
		code = 97 + (code - 97 + i) % 26
	elif 65 <= code <= 90:
		code = 65 + (code - 65 + i) % 26
	else:
		pass
	return chr(code) 
#-------------------------------------------------#
def encrytion():
	message = raw_input('Enter message: ')
	key = input('Enter key: ')
	text = ''
	for j in message:
		text += encaesar(j,key)
	print text
	text = ''
#-------------------------------------------------#
def decrytion():
	message = raw_input('Enter message: ')
	text = ''
	for i in range(27):
		for j in message:
			text += decaesar(j,i)
		print text
		text = ''
#-------------------------------------------------------------#
print "Choose menu"
print "1.Encryption"
print "2.Decryption"
choice = input()
if choice == 1:
	encrytion()
elif choice == 2:
	decrytion()
else:
	print "Error!"
