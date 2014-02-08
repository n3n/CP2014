n = input()
summary = 0
if n <= 0:
	for i in xrange(n,2):
		summary += i
else:
	for i in xrange(1,n+1):
		summary += i
print summary
