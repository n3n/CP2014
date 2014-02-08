input_i=input()
input_j=raw_input()
input_k=input_j.split()
count=0
input_m=[]

for i in input_k:
	 input_m.append(int(i))


while 0 not in input_m:
	for j in range(input_i):
		if min(input_m) == input_m[j]:
			input_m[j]+=1
			break
	for i in range(input_i):
		input_m[i]=input_m[i] - 1		
	
			
	count+=1
	
	
print count
