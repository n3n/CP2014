def sub_table(pos):
    ls = []
    for i_row in xrange((pos[0]/3 * 3), (pos[0]/3 * 3)+3):
        for i_column in xrange(pos[1]/3 *3, (pos[1]/3 * 3)+3):
            if i_row == pos[0] and i_column == pos[1]:
                ls.append(pos[2])
            else:
                ls.append(table[i_row][i_column])
    return ls

def sub_grid(pos):
    row = table[pos[0]]
    column = []
    for i in xrange(9):
        column.append(table[i][pos[1]])
    row[pos[1]] = pos[2]
    column[pos[0]] = pos[2]
    gp = sub_table(pos)
    return row, column, gp


def sudoku_accept(pos):
    row, column, gp =  sub_grid(pos)
    if row.count(0) > 0     or \
       column.count(0) > 0  or \
       gp.count(0) > 0:
        return False
    return True

def sudoku_reject(pos):
    row, column, gp = sub_grid(pos)
    for i in xrange(1,10):
        if row.count(i) > 1     or \
           column.count(i) > 1  or \
           gp.count(i) > 1:
            return True
    return False

def sudoku_way(pos):
    row, column, gp =  sub_grid(pos)
    ls = []
    for i in xrange(1,10):
        if not i in row     and \
           not i in column  and \
           not i in gp:
            ls.append(i)
    return ls

def sudoku_beam_kill():
    # 1. Get sub table 9 table
    # 2. Find number in way_solution is not have in another member
    # 3. Set table this position to this value
    for gp_row in xrange(3):
        for gp_column in xrange(3):
            pos = [gp_row*3, gp_column*3]
            pos.append(table[pos[0]][pos[1]])
            gp = sub_table(pos)

            # Get zero slot.
            print 'index_zero get index from pos_problem'
            index_zero = []
            for i in xrange(9):
                if gp[i] != 0:
                    continue
                index_zero.append(pos_problem.index([pos[0]+i/3, pos[1]+i%3]))
                print pos_problem[index_zero[-1]]

            # Find number in another way on this gp.
            del_ways = []
            for i in index_zero:
                for itr in index_zero:
                    if i == itr or itr in del_ways or len(way_solution[i]) <= 1:
                        continue
                    ways = way_solution[i]
                    for way in ways:
                        isHave = False
                        for other_way in way_solution[itr]:
                            if other_way == []:
                                continue
                            if (isinstance(other_way, list) and way in other_way) or \
                               (isinstance(other_way, int) and way == other_way):
                                isHave = True
                                break
                        if not isHave:
                            pos_i = pos_problem[i]
                            print 'pos change:, pos_i, way
                            table[pos_i[0]][pos_i[1]] = way
                            pos_problem[i] = []
                            way_solution[i] = []
                            break

            # Del way_solution this used.
            print 'pos_prob & way_solu'
            pos_problem.sort()
            way_solution.sort()
            #print pos_problem
            #print way_solution
            while pos_problem and pos_problem[0] == []:
                del pos_problem[0]
                del way_solution[0]
            print pos_problem
            print way_solution 

            for i in xrange(9):
                print table[i]
            print ''

def sudoku_bt(pos, n):
    #if sudoku_reject(pos):
    #    print 'Reject'
    #    return False
    if sudoku_accept(pos):
        print 'Accept'
        return True
    elif n == limit_way:
        #print 'Fuck! it\'s wrong.'
        #print table[0]
        return False
    ls_way = way_solution[n]
    for i in ls_way:
        pos[2] = i
        table[pos[0]][pos[1]] = pos[2]
        if sudoku_bt(pos, n+1):
            print 'Finish'
            return True
        #value = sudoku_bt(pos, n+1)
        #if isinstance(value, list):
        #    return value

table = []
way_solution = []
pos_problem = []
for i_row in xrange(9):
    table.append(map(int, list(raw_input())))

for i_row in xrange(9):
    for i_column in xrange(9):
        if table[i_row][i_column] == 0:
            way_solution.append(sudoku_way([i_row, i_column, 0]))
            if len(way_solution[-1]) == 1:
                table[i_row][i_column] = way_solution[-1][0]
                del way_solution[-1]
            else:
                pos_problem.append([i_row, i_column])
limit_way = len(way_solution)
total = 1
for i in xrange(limit_way):
    total *= len(way_solution[i])
    print pos_problem[i], way_solution[i]
print total

sudoku_beam_kill()
print 'Beam kill'
for i in xrange(9):
    print table[i]
print ''

limit_way = len(way_solution)
total = 1
for i in xrange(limit_way):
    total *= len(way_solution[i])
    print total

if limit_way > 0:
    p = pos_problem[0]
    p.append(0)
    #sudoku_bt(p, 0)

print 'Result:'
for i in xrange(9):
    print table[i]
