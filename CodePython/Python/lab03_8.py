def is_prime(n):
	'''If n is prime return True, False otherwise'''
	for i in xrange(2, n):
		if n % i == 0:
			return False
	return True

print is_prime(input('Number: '))