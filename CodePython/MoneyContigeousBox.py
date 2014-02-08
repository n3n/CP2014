data = []
for i in xrange(input()):
	data.append(input())

maxnearsum = 0
maxfarsum = 0
negative = True
for i in data:
	maxnearsum = max(maxnearsum + i, 0)
	maxfarsum = max(maxnearsum, maxfarsum)
	if i >= 0:
		negative = False
if negative:
	print max(data)
else:
	print maxfarsum
