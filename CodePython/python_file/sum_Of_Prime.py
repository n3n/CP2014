import math
alist = [2,3,5,7,11,13]

def checkPrime(i):
	for j in range(3,int(math.sqrt(i))):
		if i % j == 0:
			return False
	return True
	
for i in range(19,1002):
	if checkPrime(i):
		alist.append(i)
		
print sum(alist)
