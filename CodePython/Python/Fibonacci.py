memo = { 0:0, 1:1 }
def fibo(n):
	if not n in memo:
		memo[n] = fibo(n-1) + fibo(n-2)
	return memo[n]

print fibo(input())