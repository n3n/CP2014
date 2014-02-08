m = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
cnt = 0
for n in range(input()):
	for i in raw_input().split():
		for j in i:
			if j in m:
				cnt += 1
				break
print cnt
