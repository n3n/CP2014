alist = []
key = 2
n = input()
m = n
while n > 1:
	while n % key == 0:
		alist.append(str(key))
		n /= key
	key = key + 1
	if key*key > n:
		if n > 1:
			alist.append(str(n))
			break
print m,'=',' x '.join(alist) 
