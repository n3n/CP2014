test = input()
for case in xrange(test):
	data = raw_input()
	weight = raw_input()
	data = data.split()
	n = int(data[0])
	p = int(data[1])
	q = int(data[2])
	weight = weight.split()
	weight = [ int(each) for each in weight ]
	weight.sort()
	cp = 0
	cq = 0
	while cp <= n and cp < p and cq <= q and cp < len(weight):
		if cq + weight[cp] <= q:
			cq += weight[cp]
			cp += 1
		else:
			break
	print 'Case ' + str(case + 1) + ': ' + str(cp)
	 	 