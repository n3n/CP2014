input_i=raw_input()

input_j=input_i.replace("[", " ");
input_k=input_j.replace("]", " ");
input_l=input_k.replace(",", " ");
input_m=input_l.split()

new=[]
for i in input_m:
	new.append(int(i))
print max(new)
