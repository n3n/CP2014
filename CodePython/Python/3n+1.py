while True:
	n = input()
	if n == 0:
		break
	c = 1
	while n != 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = ( 3 * n ) + 1
		c += 1
	print c