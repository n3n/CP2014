txt = raw_input()
i = 0
out = ''
aei = ['a', 'e', 'i', 'o', 'u']
for x in txt:
	if x.lower() in aei:
		if i % 2 == 0:
			out += 'A'
		else:
			out += 'a'
	else:
		out += x
	i += 1

print out