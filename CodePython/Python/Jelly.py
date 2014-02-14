raw = raw_input()
jelly = raw.split(" ")
for x in xrange(len(jelly)):
	jelly[x] = int(jelly[x])
count = 0
jelly.sort()
while jelly[-1] != 1:
	jelly[-1] = jelly[-1] / 2	
	jelly.sort()
	count += 1
print count