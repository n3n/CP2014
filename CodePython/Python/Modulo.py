d = []
for e in xrange(input()):
	tmp = input() % 42
	if not tmp in d:
		d.append(tmp)
print len(d)