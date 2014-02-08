def qe(a,b,c):
    results = []
    in_root = b**2 - 4*a*c
    if in_root > 0:
        print '%.4g' % ((-b-math.sqrt(in_root))/(2*a))
        print '%.4g' % ((-b+math.sqrt(in_root))/(2*a))
    elif in_root < 0:
        print "complex root"
    else:
        print '%.4g' % (-b/(2.0*a))

import math

qe(input(), input(), input())
