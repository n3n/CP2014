dic = dict()
n = input()
ls = raw_input().split()
for i in ls:
	if not int(i) in dic:
		dic[int(i)] = 1
	else:
		dic[int(i)] += 1

most_value = max(dic.values())
while most_value in dic.values():
	print dic.keys()[dic.values().index(most_value)],
	del dic[dic.keys()[dic.values().index(most_value)]]