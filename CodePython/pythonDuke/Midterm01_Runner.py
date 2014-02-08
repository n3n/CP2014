input_i,input_j=input(),input()
ans=[]
for i in range(input_j):
	data=raw_input()
	speed,distance=data.split()
	ans.append(((input_i-float(distance))/float(speed),i+1))

ans.sort()	
print ans[0][1]		
