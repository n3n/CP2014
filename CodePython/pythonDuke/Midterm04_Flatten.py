input_i=raw_input()
an=[]
an1=[]
ab=[]
input_j=input_i.replace("[", " ");
input_k=input_j.replace("]", " ");
input_l=input_k.replace(",", " ");
input_m=input_l.split()

count=0
while len(input_m)>count:
	an.append(int(input_m[count]))
	ab.append(int(input_m[count]))
	count+=1

count1=0

while len(ab)>count1:
	an1.append(max(an))
	an.remove(max(an))
	count1+=1
print an1
