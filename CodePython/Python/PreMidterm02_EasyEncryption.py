txt = raw_input()
out = ''
for x in txt:
	o = ord(x)
	if o >= 97 and o <= 122:
		t = str(o - 96)
		if len(t) < 2:
			t = '0' + t
		out += t
	elif o >= 65 and o <= 90:
		t = str(o - 38)
		if len(t) < 2:
			t = '0' + t
		out += t
	elif o >= 48 and o <= 57:
		out += '#' + x
	else:
		out += x
print out