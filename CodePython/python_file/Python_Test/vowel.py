ls = list(raw_input())
deli = "aeiouAEIOU" #10
len_ls = len(ls) - 1
while len_ls >= 0:
	for i in xrange(10):
		if ls[len_ls] == deli[i]:
			del ls[len_ls]
			break
	len_ls -= 1

print ''.join(ls)