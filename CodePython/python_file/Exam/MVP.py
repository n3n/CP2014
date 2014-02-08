max_value = 0.0
max_name = ''
for i in xrange(input()):
	name, value = raw_input().split()
	if float(value) > max_value:
		max_name = name
		max_value = float(value)

if max_name != '':
	print max_name