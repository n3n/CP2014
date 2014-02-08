def check(num):
	for i in xrange(2, num+1):
		square = i ** 2
		if square > num:
			return True
		if num % square == 0:
			return False
	return True

count = 0
for i in xrange(1, input()+1):
	if check(i):
		count += 1
print count
