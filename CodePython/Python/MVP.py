data = {}
enemy = input()
for x in xrange(enemy):
	target = raw_input()	
	targetsp = target.split(" ")
	data[targetsp[0]] = int(targetsp[1])
dataval = data.values()
dataval.sort()
sort = []
for dv in dataval:
	for na in data:
		if data[na] == dv:
			sort.append(na)
if len(sort) > 0:
	print sort[-1]