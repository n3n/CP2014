roman = raw_input()
char = (('M',  1000), ('CM', 900), ('D',  500), ('CD', 400), ('C',  100), ('XC', 90), ('L',  50), ('XL', 40),('X',  10), ('IX', 9), ('V',  5),  ('IV', 4), ('I',  1))
res, index = 0, 0
for num, val in char:
	count = 0
	while roman[index: index +len(num)] == num:
		count += 1
		res += val
		index += len(num)
print res