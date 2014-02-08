for sets in xrange(input()):
    rows = input()
    width = input()
    min_Val = int
    alist = []
    for row in xrange(rows):
        alist.append(raw_input())
    for brute in xrange(1,width+1):
        cnt = 0
        for block in alist:
            cnt += abs(int(block) - brute)
        #print "Block move",cnt
        if cnt < min_Val:
            min_Val = cnt
            #print "min_Val = ",min_Val
    print min_Val
