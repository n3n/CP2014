alist, alist2 = [], []
n = input()
if n == 0:
	print 'NONE','NONE'
elif n == 1:
	print 0, 'NONE'
else:
	for i in xrange(n):
		k = input()
		alist.append(k)
		alist2.append(k)
	alist2.sort()
	min_Value = min(alist2)
	for j in range(min_Value):
		if j != min_Value:
			print min_Value,j
		alist2.remove(j)
	#else:
	#	print alist.index(alist2[0]),alist.index(alist2[1])

