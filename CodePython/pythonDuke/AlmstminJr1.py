n = input()
ls = []
for i in xrange(n):
    ls.append(input())
if n==0:
    print 'NONE '*2
elif n==1:
    print '0 NONE'
else:
    n_min, n_min2 = sorted(ls)[:2]
    print ls.index(n_min), ls.index(n_min2)
