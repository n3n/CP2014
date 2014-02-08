cnt = 0
def fibo(n):
	global cnt,r
	#print "Fibonacci : " + str(n)
	if n == r:
		cnt += 1
	if n == 0 :
		if r == n:
			return 1
		return 0
	if n == 1 :
		if r == n:
			return 1
		return 0
	else:
		result = (fibo(n-1)) + (fibo(n-2))
		return cnt
n,r = input(),input()
#print fibo(n)

for i in range(n):
	print fibo(n)
