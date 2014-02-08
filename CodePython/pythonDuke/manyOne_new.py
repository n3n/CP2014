s = [0, '1', '11']
n = input()
for i in xrange(3,n+1):
    s.append(s[i-1] + s[i-2])
#for i in xrange(1,n+1):
#    print 'S'+str(i), '=', s[i]
print s[n]
