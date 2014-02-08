def caesar(character,i):
	a = ord(‘a’)
	z = ord(‘z’)
	A = ord(‘A’)
	Z = ord(‘Z’)
	code = ord(character)
	if a <= code <= z:
		code = a + (code - a + i) % 26
	elif A <= code <= Z:
		code = A + (code - A + i) % 26
	else:
		pass
	return chr(code)
caesar('a',2)
