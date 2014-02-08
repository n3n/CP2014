def ManyOne(n):
	if n == 1:
		return '1'
	elif n == 2:
		return '2'
	s1 = '1'
	s2 = '2'
	for i in xrange(n-2):
		s1, s2 = s2, s1 + s2
	return s2

print ManyOne(input())
