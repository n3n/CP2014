def prime_v0(n):
	if n == 1:
		return False
	for i in range(2,int(n**0.5)):
		if n % i == 0:
			return False
	return True
print prime_v0(input())
