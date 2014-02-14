l1 = raw_input()
l2 = raw_input()
if len(l1) != len(l2):
	dif = abs(len(l2) - len(l1))
	if len(l1) < len(l2):
		l1 = ('0' * dif ) + l1
	else:
		l2 = ('0' * dif ) + l2
i = 0
s = 0
while i < len(l1):
	s += int(l1[i]) * int(l2[i])
	i += 1
print s