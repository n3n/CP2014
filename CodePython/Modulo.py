alist = []
for i in xrange(input()):
	n = input()%42
	if n not in alist:
		alist.append(n)
print len(alist)
