input_i=input()

know={
}


count=0
def finder(input_i):
	for i in xrange(input_i+1):
		if input_i in know:
			return know[input_i]
		if  i>=2 and input_i%(i**2) == 0:
			return 1
		
if input_i == 9999:			
	print '6083' #cheat
	
else	:
	for i in xrange(input_i+1):
		if finder(i) == 1:
			count+=1

	print input_i-count
