def print_matrix(row, column):
	if row > 0:
		travel_column(column)
		print ''
		print_matrix(row-1, column)

def travel_column(column):
	if column > 0:
		print raw_input(),
		travel_column(column-1)

row = input()
column = input()
print_matrix(row, column)
