def gcd(a, b):
	return b and gcd(b, a % b) or a

print gcd(12, 14)
