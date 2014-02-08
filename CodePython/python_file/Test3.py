line1 = raw_input()
line2 = raw_input()
line3 = raw_input()
def XO(line1,line2,line3):
    if line1[0] + line2[0] + line3[0] == 'XXX' or line1[0] + line2[0] + line3[0] == 'OOO':
        return line1[0] + ' |'
    elif line1[1] + line2[1] + line3[1] == 'XXX' or line1[1] + line2[1] + line3[1] == 'OOO':
        return line1[1] + ' |'
    elif line1[2] + line2[2] + line3[2] == 'XXX' or line1[2] + line2[2] + line3[2] == 'OOO':
        return line1[2] + ' |'
    elif line1[0] + line2[1] + line3[2] == 'XXX' or line1[0] + line2[1] + line3[2] == 'OOO':
        return line1[0] + ' \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'
    elif line1[2] + line2[1] + line3[0] == 'XXX' or line1[2] + line2[1] + line3[0] == 'OOO':
        return line1[2] + ' /'
    elif line1 == 'XXX' or line1 == 'OOO':
        return line1[0] + ' -'
    elif line2 == 'XXX' or line2 == 'OOO':
        return line2[0] + ' -'
    elif line3== 'XXX' or line3 == 'OOO':
        return line3[0] + ' -'
    else:
        return 'Draw'


print XO(line1,line2,line3)
