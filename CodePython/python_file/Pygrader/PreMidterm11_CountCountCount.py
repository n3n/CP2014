dic = {'a':0,'e':0,'i':0,'o':0,'u':0}
alist = ['a','e','i','o','u']
for i in xrange(input()):
	for i in raw_input(): 
		if i in ['a','e','i','o','u','A','E','I','O','U']:
			dic[i.lower()] += 1
for k in alist:
	print k+':',dic[k]
