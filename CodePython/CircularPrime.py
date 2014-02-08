import math

def is_prime(n):
	if n == 1:
		return False
	for i in xrange(2, int(math.sqrt(n)+1)):
		if n % i == 0:
			return False
	return True
	
def is_circular(n):
	cnt = 0
	primes = []
	for i in range(len(str(n))):
		primes.append(str(n)[i:] + str(n)[:i])
	for j in primes:
		if is_prime(j):
			cnt += 1
	if cnt == len(str(n)):
		return True,primes
	return False

def CircularPrime(n):
	alist = []
	cnt = 0
	for i in xrange(2,n+1):
		if is_prime(i) and i not in alist:
			if is_circular(i):
				cnt += 1
			
		#~ if is_prime(int(i)) and i not in alist:
			#~ if is_circular(i):
				#~ cnt += 1
	return cnt
	
print CircularPrime(input())
			
