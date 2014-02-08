def next_pos(row, column):
    column += 1
    if column > 8:
        column = 0
        row += 1
    return row, column

def sub_table(row, column):
    ls = []
    for i_row in xrange(row/3 * 3, (row/3 * 3)+3):
        for i_column in xrange(column/3 *3, (column/3 * 3)+3):
            ls.append(table[i_row][i_column])
    return ls

def sub_grid(row, column):
    grid_row = table[row]
    grid_column = []
    for i in xrange(9):
        grid_column.append(table[i][column])
    gp = sub_table(row, column)
    return grid_row, grid_column, gp

def n_most_same(ls):
    dic = defaultdict(int)
    for i in ls:
        dic[i] += 1
    dic[0] = 0
    return max(dic.values())

def chk_table(row, column):
    grid_row, grid_column, gp = sub_grid(row, column)
    #if n_most_same(grid_row) > 1    or \
    #   n_most_same(grid_column) > 1 or \
    #   n_most_same(gp) > 1:
    if grid_row.count(table[row][column]) > 1       or \
       grid_column.count(table[row][column]) > 1    or \
       gp.count(table[row][column]) > 1:
        return False
    return True

def sudoku_bt(row, column):
    #num[0] = num[0] + 1
    if row == 9 and column == 0:
        #print 'Finish'
        return True
    next_row, next_column = next_pos(row, column)
    if table[row][column] != 0:
        return sudoku_bt(next_row, next_column)
    for i in xrange(1,10):
        table[row][column] = i
        if chk_table(row, column) and sudoku_bt(next_row, next_column):
            return True
        table[row][column] = 0
    return False

#from time import time
from collections import defaultdict
#t_start = time()

table = []
for i_row in xrange(9):
    table.append(map(int, list(raw_input())))

#num = [0]
sudoku_bt(0,0)
#print num

#print 'Result:', time() - t_start
for i_row in xrange(9):
    st = ''
    for i_column in xrange(9):
        st += str(table[i_row][i_column])
    print st
