# 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 2 4 6 8 10 12 14 3 9 15 5 7 11 13


a=raw_input()
b=a.split()
input_i=int(b[0])
input_j=int(b[1])
# 15 12 >> 15 = input_i
# 12 = input_j

n_input_i=range(2,input_i+1)
b_n=n_input_i
# 15 >>> n_input_i = [2,3,4,5,6,7,8,9,10,11,12,13,14,15]

ans=[]
#

for i in n_input_i: # 2->15 type i=int
	for j in b_n: # 2->15
		if j%i == 0 and j not in ans:
			ans.append(j)

#ans
print ans[input_j-1]
