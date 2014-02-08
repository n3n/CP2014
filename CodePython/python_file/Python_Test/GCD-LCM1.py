def gcd(a,b):
	if b == 0:
		return a
	else:
		return gcd(b,a%b)

a = input()
b = input()
gcd_num = gcd(max(a,b), min(a,b))
print gcd_num
print a*b/gcd_num