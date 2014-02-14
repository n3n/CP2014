n = input() + 1
s = input() - 1
k = input() - 1

d = s
p = range(1, n)
while len(p) > 1:
	d = k % len(p) + d
	if d >= len(p):
		d = d % len(p)
	del p[d]

print p[0]