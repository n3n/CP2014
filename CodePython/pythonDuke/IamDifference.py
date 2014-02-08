total = 0
ls = []
for i in xrange(8):
    ls.append(input())
    total += ls[-1]
for n in ls:
    if total-n == 55:
        print n
        break
