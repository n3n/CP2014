n = input()
r = input()
if r == 0:
	r = 2
if n == r:
	print 1
else:
	a = 1
	b = 1
	for x in xrange(1,n):
		b, a = a + b, b
		if n - r == x:
			print a
			break