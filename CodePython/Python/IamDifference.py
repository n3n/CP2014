data = []
for i in xrange(8):
	data.append(input())

for e in data:
	comp = data[:]
	comp.remove(e)
	'''
	print 'comp',comp
	print 'sum(comp)',sum(comp)
	print 'e',e
	print '='*30
	'''
	if sum(comp) == 55:
		print e
		exit()
