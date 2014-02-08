def runner():
	d = input()
	n = input()
	runner = []
	for i in xrange(n):
		data = raw_input()
		v,s = data.split()
		t = (d-float(s))/float(v)
		runner.append((t, 1/float(v), i+1))
	runner.sort()
	print runner[0][2]
runner()
