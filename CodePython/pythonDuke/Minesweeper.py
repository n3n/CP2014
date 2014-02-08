import string

def n_bomb(row, column):
    total = 0
    for i_row in xrange(row-1, row+2):
        if i_row < 0:
            continue
        elif i_row >= n_row:
            break
        for i_column in xrange(column-1, column+2):
            if i_column < 0:
                continue
            elif i_column >= n_column:
                break
            if table[i_row][i_column] == 'x':
                total += 1
    return total
 
n_row = input()
table = []
for i in xrange(n_row):
    #table.append(string.strip(raw_input()))
    table.append(raw_input())
n_column = len(table[0])

for i_row in xrange(n_row):
    st = ''
    for i_column in xrange(n_column):
        if table[i_row][i_column] != 'x':
            num = n_bomb(i_row, i_column)
            if num == 0:
                st += ' '
            else:
                st += str(num)
        else:
            st += 'x'
    print st
