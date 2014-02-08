height = input() # cm
if height > 200 * 1000 * 100:
    print 'fried'
else:
    # convert time to min
    up = 20 * 60
    down = 7 * 60
    print 'up',up
    print 'down',down
    tmp = ((height - 10) / 3.0)
    fulltime = int(tmp)
    if not (tmp % 1 == 0 and height > 10):
        fulltime = int(tmp) + 1
    print 'fulltime',fulltime
    halftime = height - (fulltime * 3)
    print 'halftime',halftime
    totaltime = ((up + down) * fulltime) + ((up / 10) * halftime)
    print 'totaltime',totaltime
    if totaltime >= 4096 * 365 * 24 * 60:
        print 'dead'
    else:
        if totaltime % 1 != 0:
            totaltime = int(totaltime) + 1
        print totaltime 
