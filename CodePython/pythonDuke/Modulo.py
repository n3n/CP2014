n = input()
ls = [False for i in xrange(42)]
for i in xrange(n):
    ls[input()%42] = True
print ls.count(True)
