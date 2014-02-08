liza=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
sumall=0
input_i=raw_input()
input_j=input_i.split()
check=0
for i in input_j:
	dontlike=0
	for j in i:
		if j in liza :
			sumall+=1
		if j not in liza:
			dontlike+=1
			if dontlike == len(i):
				check+=1
			
			
			
if check == len(input_j):
	print '0.00'			
else:
	prom=float(sumall)/(len(input_j)-check)
	print '%.2f'%prom
