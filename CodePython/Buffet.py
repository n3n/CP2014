summary = 0
for i in xrange(8):
	n = input()
	if n != 0:
		summary += max(map(int, raw_input().split()))
print summary
