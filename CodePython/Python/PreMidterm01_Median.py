c = 1
while True:
	txt = raw_input()
	if txt == '0':
		break
	txt = txt.split(' ')
	for i in xrange(len(txt)):
		txt[i] = int(txt[i])

	lenn = len(txt[1:])
	if lenn % 2 == 0:
		print 'Case ' + str(c) +': ' + str((float(txt[ lenn / 2 ]) + txt[ (lenn / 2) + 1]) / 2)
	else:
		print 'Case ' + str(c) +': ' + str(float(txt[ lenn / 2 + 1 ]))
	c += 1