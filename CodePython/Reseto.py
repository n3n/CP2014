n, k = map(int, raw_input().split())
num, mum, alist, cnt, finish, r = [], [], [], 0, False, 0
for i in xrange(2,n+1):
	num.append(i)
	mum.append(i)
while True:
	j = num[0]
	m = j
	if finish == True:
		break
	r = 0
	if len(num) == 1:
		alist.append(num[0])
		print alist[k-1]
		break 
	for l in num:
		if l % m == 0:
			alist.append(l)
			num.remove(l)
			cnt += 1
		elif cnt == 0 and r-1 == len(num):
			alist.append(l)
		if len(alist) == k:
			print alist[-1]
			finish = True
			break
		r += 1
	if len(alist) == len(mum):
		print alist[k]
		break
