known = {0:0, 1:1}
def fibo(n):
	if n in known:
		return known[n]
	res = fibo(n-1) + fibo(n-2)
	known[n] = res
	return res
n = input()
print fibo(n)
