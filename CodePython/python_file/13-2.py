table = []

for i in range(9):
	x = raw_input()
	row = []
	for i1 in x:
		row.append(i1)
	table.append(row)

def findzero(table):
	re = []
	for i in range(9):
		for i1 in range(9):
			if table[i][i1] == '0':
				a = []
				a.append(i)
				a.append(i1)
				re.append(a)
	return re

def iff(x,y,table):
	row = ""
	for i in table[x]:
		row += str(i)

	col = ""
	for i in range(9):
		col += str(table[i][y])

	box = ""
	for i in range(3):
		for i1 in range(3):
			box += str(table[(3*(x/3))+i][(3*(y/3))+i1])

	re = []
	for i in range(1,10):
		if not str(i) in col and not str(i) in row and not str(i) in box:
			#print c , r , " = " , i
			re.append(str(i))
	return re
	print re


def sudoku(table,blank,n=0):
	if len(findzero(table)) < 1:
		return "s"
	else:
		point = blank[n]
		a = iff(point[0],point[1],table)
		#print a ,point
		if len(a) == 0:
			return "f"
		else:
			for i in a:
				#print i,point
				table[point[0]][point[1]] = str(i)
				b = sudoku(table,blank,n+1)
				if b == "f":
					table[point[0]][point[1]] = '0'
				elif b == "s":
					return b
			return "f"
#print len(findzero(table))
sudoku(table,findzero(table))
for c in range(9):
	row = ""
	for i in table[c]:
		row += str(i)
	print row
