input()
looplike = map(int, raw_input().split())
d = dict()

for i in looplike:
	if i not in d:
		d[i] = 1
	else:
		d[i] += 1
		
max_Like = max(d.values())
like = []

for i in d:
	if d[i] == max_Like:
		like.append(str(i))
		
print ' '.join(like)
