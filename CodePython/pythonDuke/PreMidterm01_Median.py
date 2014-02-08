n = 0
line = 1
ls = []
while True:
    ls = []
    ls = map(float, raw_input().split())
    n = int(ls.pop(0))
    if n == 0:
        break
    ls.sort()
    if n%2 == 0:
        print 'Case', str(line)+':', ( ls[(n)/2 - 1]+ls[(n)/2+1 - 1] ) / 2
    else:
        print 'Case', str(line)+':', ls[(n+1)/2 - 1]
    line += 1
