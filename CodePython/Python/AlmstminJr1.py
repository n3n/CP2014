n = input()
if n > 1:
	d = []
	for e in xrange(n):
		d.append(input())
	rmin = d.index(min(d))
	d[rmin] = max(d) * 2
	amin = d.index(min(d))
	print rmin, amin
elif n > 0:
	print '0 NONE'
else:
	print 'NONE NONE'