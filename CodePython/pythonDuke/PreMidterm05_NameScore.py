def cal_score(st):
    total = 0
    for ch in st:
        total += ord(ch) - 64
    return total

for i in xrange(1,input()+1):
    print 'Name', i, ':', cal_score(raw_input())*i
