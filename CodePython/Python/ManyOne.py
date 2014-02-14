n = input()
if n == 1:
	print '1'
elif n == 2:
	print '11'
else:
	s1 = '1'
	s2 = '11'
	for i in xrange(n - 2):
		s1, s2 = s2, s1 + s2
	print s2