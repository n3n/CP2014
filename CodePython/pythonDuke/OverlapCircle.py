from math import sqrt

def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

x1, y1, r1 = input(), input(), input()
x2, y2, r2 = input(), input(), input()
#print distance(x1, y1, x2, y2)
if distance(x1, y1, x2, y2) > r1+r2:
    print "no overlapping"
else:
    print "overlapping"
