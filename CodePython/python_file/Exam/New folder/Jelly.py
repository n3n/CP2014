j1,j2,j3 = list(raw_input().split())
j1,j2,j3 = int(j1),int(j2),int(j3)
count = 0
while j1 != 1:
	j1 /= 2
	count += 1
	if j1 == 2:
		j1 = 1
		count += 1
while j2 != 1:
	j2 /= 2
	count += 1
	if j2 == 2:
		j2 = 1
		count += 1
while j3 != 1:
	j3 /= 2
	count += 1
	if j3 == 2:
		j3 = 1
		count += 1
print count