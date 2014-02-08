string = ''
for i in xrange(1,13):
    print '',
    for j in xrange(1,13):        
        a = ' '*(3-len(str(i*j)))+'%s' % str(i*j)
        string += a+' '
    print string[:-1]
    string = ''
