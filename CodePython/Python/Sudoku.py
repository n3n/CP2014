def chkrow():
	pass

def chkcol():
	pass

sudoku = []
for x in xrange(9):
	raw = raw_input()
	sudoku.append([e for e in raw])



for row in sudoku:
	for col in row:
		if col == 0:


print sudoku