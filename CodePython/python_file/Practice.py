def num_in_str(message):
	for i in message.split():
		try:
			if i[-1] == '.' and i[0] != '.':
				if isinstance(float(i[:-1]),float) or isinstance(int(i[:-1]),int):
					return i[:-1]
			elif i[0] == '.' and i[-1] != '.':
				if isinstance(float(i[1:]),float) or isinstance(int(i[1:]),int):
					return i[1:]
			elif i[0] == '.' and i[-1] == '.':
				if isinstance(float(i[1:-1]),float) or isinstance(int(i[1:-1]),int):
					return i[1:-1]
			elif isinstance(float(i),float) or isinstance(int(i),int):
				return i
		except:
				continue
			
print num_in_str('abcad 123 asdadsad')
print num_in_str('asdasd 123. asdadas')
print num_in_str('asdasd 1.23 asdasdas')
print num_in_str('asdas .123. asdasd')
print num_in_str('asdasd .123 asdasd')
print num_in_str('asdasd .12.3 asdasd')
print num_in_str('asdasd .1.23. asdasd')
