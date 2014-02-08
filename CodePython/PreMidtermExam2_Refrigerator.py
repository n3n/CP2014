n = input()
l = raw_input().split()
alist = []
num,cnt = 0,0
for i in l:
	alist.append(int(i))
while 1:
	minValue = alist.index(min(alist))
	for i in range(len(alist)):		
		alist[i] -= 1
	alist[minValue] += 1
	cnt += 1
	if 0 in alist:
		break
	num += 1
print cnt
