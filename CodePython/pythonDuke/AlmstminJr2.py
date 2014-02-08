n = input()
ls = []
for i in xrange(n):
    ls.append(input())
if n==0:
    print 'NONE '*2
else:
    ls_sort = list(set(ls))
    ls_sort.sort()
    if len(ls_sort) < 2:
        print 0, 'NONE'
    else:
        n_min, n_min2 = ls_sort[:2]
        print ls.index(n_min), ls.index(n_min2)
