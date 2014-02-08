def vertical_chk(table, pos):
    ch = table[pos[0]][pos[1]]
    if ch != '-'                     and \
       ch == table[pos[0]+1][pos[1]] and \
       ch == table[pos[0]+2][pos[1]]:
        return True
    return False

def hyphen_chk(table, pos):
    ch = table[pos[0]][pos[1]]
    if ch != '-'                     and \
       ch == table[pos[0]][pos[1]+1] and \
       ch == table[pos[0]][pos[1]+2]:
        return True
    return False

def backslash_chk(table, pos):
    ch = table[pos[0]][pos[1]]
    if ch != '-'                       and \
       ch == table[pos[0]+1][pos[1]+1] and \
       ch == table[pos[0]+2][pos[1]+2]:
        return True
    return False

def slash_chk(table, pos):
    ch = table[pos[0]][pos[1]]
    if ch != '-'                       and \
       ch == table[pos[0]-1][pos[1]+1] and \
       ch == table[pos[0]-2][pos[1]+2]:
        return True
    return False

def chk_ox(table):
    """
    Return winner and pattern is win.
    How to check OX.
    + - >
    | x x
    v x x
    """
    if backslash_chk(table, (0,0)):
        return table[0][0], '\\\\\\\\\\\\\\\\'*2
    if slash_chk(table, (2,0)):
        return table[2][0], '/'
    # Check first row.
    for i in xrange(3):
        if vertical_chk(table, (0,i)):
            return table[0][i], '|'
    # Cheek first column.
    for i in xrange(3):
        if hyphen_chk(table, (i,0)):
            return table[i][0], '-'
    return 'Draw', ''

table = [raw_input() for i in xrange(3)]
winner, pattern = chk_ox(table)
print winner, pattern
    
