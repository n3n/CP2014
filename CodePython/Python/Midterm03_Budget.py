
man, work = raw_input().split()
worker = {}
workdata = {}
for i in xrange(int(man)):
	num, level, budget = raw_input().split()
	worker[int(level)] = int(budget)

totalbudget = 0
for i in xrange(int(work)):
	working, time = raw_input().split()
	working = int(working[1:])
	time = int(time)
	if working in workdata:
		workdata[working] += time
	else:
		workdata[working] = time
	totalbudget += worker[working] * time
eachtime = workdata.values()
print totalbudget, max(eachtime)
