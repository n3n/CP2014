def chk(li):
	ret = []
	for each in li:
		if isinstance(each, list):
			each = chk(each)
		ret.append(each)
	return max(ret)

print chk(input())