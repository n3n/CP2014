def swap(n):
	ret = [n]
	n = str(n)
	for x in xrange(len(n) - 1):
		n = n[1:] + n[0]
		ret.append(int(n))
	return ret

def isprime(n):
	if n == 1:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True

print swap(input())