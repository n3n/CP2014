string = ''
def encaesar(character,key):
	global string
	a = ord('a')
	z = ord('z')
	A = ord('A')
	Z = ord('Z')
	code = ord(character)
	for i in range(1,27*key,key):
		if a <= code <= z:
			code = a + (code - a + i) % 26
		elif A <= code <= Z:
			code = A + (code - A + i) % 26
		else:
			pass
		string += chr(code)

def encrytion():
	key = input('Enter key: ')
	message = raw_input('Enter message: ')
	text = ''
	for j in message:
		text += encaesar(j,key)
	print text
	text = ''
#message = raw_input()
encrytion()
