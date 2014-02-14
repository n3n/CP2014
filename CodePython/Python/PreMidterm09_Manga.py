def chk(li):
	ret = []
	for each in li:
		if isinstance(each, list):
			each = chk(each)
		ret.append(each)
	return ret[::-1]

print chk(input())