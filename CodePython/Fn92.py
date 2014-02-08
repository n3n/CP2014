def Fn92(h):
    if h == 1:
        return 3
    elif h == 2 or h == 3:
        return 1
    elif h % 2 == 0:
        pass
    elif h % 2 == 1:
        pass
        
    
for i in xrange(input()):
    print Fn92(input())
