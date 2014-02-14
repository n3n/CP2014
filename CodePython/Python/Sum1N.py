n = input()
if n > 1:
	s = 0
	i = 1
	while i != n:
		s += i
		i += 1
	s += i
elif n < 1:
	s = 0
	i = 1
	while i != n:
		s += i
		i -= 1
	s += i
else:
	s = 1
print s