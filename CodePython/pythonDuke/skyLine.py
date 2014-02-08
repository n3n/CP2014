n = input()
skyline = [0 for i in xrange(10001)]
p_start = 0
p_stop = 0
p_last = 0
buding_height = 0
for i in xrange(n):
    p_start, buding_height, p_stop = map(int, raw_input().split())
    p_last = max(p_last, p_stop)
    for pos in xrange(p_start, p_stop):
        skyline[pos] = max(skyline[pos], buding_height)

#print skyline[1:p_last+1]
height = 0
for i in xrange(1, p_last+1):
    if height != skyline[i]:
        print i, skyline[i],
        height = skyline[i]
