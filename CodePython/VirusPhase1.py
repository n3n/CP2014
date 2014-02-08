n = raw_input()
try:
    binary = str(bin(int(n, 16)))
    if '10010110' in binary:
        print 'D'
    else:
        print 'S'
except:
    print 'Error'
