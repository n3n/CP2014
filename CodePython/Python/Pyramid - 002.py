h = input()

j = 0
for i in xrange(h):
	tmp = (' ' * (h - i - 1)) + '1' + ('0' * j)
	if i == 0:
		print tmp
	else:
		print tmp + '1'
	if j == 0:
		j += 1
	else:
		j += 2
