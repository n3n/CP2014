alist = []
for i in range(input()):
	alist.append(input())
min_Num = min(alist)
max_Num = max(alist)
for j in range(min_Num,max_Num):
	if j not in alist:
		print j
		break
