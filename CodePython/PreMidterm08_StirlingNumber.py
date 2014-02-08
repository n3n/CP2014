alist = [][]
n = input()
def S(n,k):
	global alist
	if n == 0 and k == 0:
		return 1
	if n == k:
		return 1
	if k == 0 and n >= 1:
		return 0
	if k > n:
		return 0
	alist.append(k*(S(n-1, k)))
	alist1.append(S(n-1, k-1))
for k in range(2,n+1):
	  S(n,k)
print alist
