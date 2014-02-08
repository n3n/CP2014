def prime_v0(n):
	if n == 1:
		return False
	for i in range(2,n):
		if n % i == 0:
			return False
	return True
#print prime_v0(input())

def prime_v1(n):
	if n == 1:
		return False
	for i in range(2,(int(n**0.5) + 1)):
		if n % i == 0:
			return False
	return True
#print prime_v1(input())

def prime_v2(n):
	cnt = 0
	for i in range(2,n+1):
		if prime_v0(i):
			cnt += 1
	return cnt		
print prime_v2(input())
	
