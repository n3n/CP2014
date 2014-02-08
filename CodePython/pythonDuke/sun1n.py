input_i=input()
sumall=0
if input_i >=1:
	for i in xrange(1,input_i+1):
		sumall=sumall+i
else:
	for j in xrange(input_i,2):	
		sumall=sumall+j
		
print sumall		
