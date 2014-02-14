def sum_odd(n):
	'''Return summation from 1 to n (sum only odd number)'''
	i = 1
	summation = 0
	while i <= n:
		if i % 2 == 1:
			summation += i
		i += 1
	return summation

print sum_odd(input('Number: '))