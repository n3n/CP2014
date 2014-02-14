n = input()
if n > 1:
	d = []
	for e in xrange(n):
		d.append(input())
	fmin = min(d)
	rmin = d.index(fmin)
	omax = max(d) * 2
	d[rmin] = omax
	while fmin == min(d):
		d[d.index(min(d))] = omax
	lmin = min(d)
	amin = d.index(lmin)
	if rmin == amin:
		print '0 NONE'
	else:
		print rmin, amin
elif n > 0:
	print '0 NONE'
else:
	print 'NONE NONE'