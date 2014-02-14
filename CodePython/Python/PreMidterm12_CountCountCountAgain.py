n = input()
c = '0123456789abcdefghijklmnopqrstuvwxyz'
w = 0
def chk(s):
	for l in s:
		if l.lower() in c:
			return True
	return False

for e in xrange(n):
	t = raw_input().split()
	for s in t:
		if chk(s):
			w += 1

print w