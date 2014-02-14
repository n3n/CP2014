n = input()
raw = raw_input()
raw = raw.split(" ")
data = {}
for x in raw:
	if x != "":
		if x in data:
			data[x] += 1
		else:
			data[x] = 1
like = data.values()
like.sort()
maxlike = like[-1]
sortlike = []
for x in data:
	if data[x] == maxlike:
		sortlike.append(int(x))
sortlike.sort()
out = ""
for x in sortlike:
	out = out + str(x) + " "
print out