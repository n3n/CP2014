for i in xrange(input()):
    a,b,n = map(int, raw_input().split())
    alist = []
    for i in xrange(1,n+1):
        if i % a == 0 and i % b != 0:
            alist.append('F')
        elif i % a != 0 and i% b == 0:
            alist.append('B')
        elif i % a == 0 and i % b == 0:
            alist.append('FB')
        else:
            alist.append(str(i))
    print ' '.join(alist)
