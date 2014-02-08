alist, alist2, a, syn = [], [], [], False
n = input()
if n == 0:
	print 'NONE','NONE'
elif n == 1:
	print '0','NONE'
else:
	for i in xrange(n):
		k = input()
		alist.append(k)
		alist2.append(k)
		a.append(k)
	
	min_Value = min(alist)
	alist2.sort()
	for m in alist2:
		if m != min_Value:
			print alist.index(min_Value),alist.index(m)
			syn = False
			break
		syn = True
	if syn == True:
		print alist.index(min_Value), "NONE"
	

