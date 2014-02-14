def sum_number_v2(n1, n2):
	'''Return summation from n1 to n2'''
	i = n1
	summation = 0
	while i <= n2:
		summation += i
		i += 1
	return summation

print sum_number_v2(input('Number1: '), input('Number2: '))