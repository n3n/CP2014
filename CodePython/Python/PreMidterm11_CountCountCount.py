n = input()
o = ['a','e','i','o','u']
a = { 'a':0, 'e':0, 'i':0, 'o':0, 'u':0 }
i = 'aeiou'
for e in xrange(n):
	t = raw_input()
	for l in t:
		if l.lower() in i:
			a[l.lower()] += 1

for k in o:
	print k + ':',a[k]