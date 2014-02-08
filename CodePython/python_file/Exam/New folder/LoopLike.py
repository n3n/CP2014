num = input()
ll = map(int,raw_input().split())

def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d

def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse
d = invert_dict(histogram(ll))
#print d
for i in d[max(d.keys())]:
	print i,