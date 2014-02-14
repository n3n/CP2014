n = input()
f = raw_input()
f = f.split()
f = [ int(each) for each in f ]
f.sort()
d = 0
if f[0] == 0:
	print 0
else:
	while not 0 in f:
		f = f[:1] + [ each - 1 for each in f[1:] ]
		f.sort()
		d += 1
	print d