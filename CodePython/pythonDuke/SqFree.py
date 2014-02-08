def isSqFree(n):
    for i in xrange(2,int(n**0.5)+1):
        if n%(i**2) == 0:
            return False
    return True

total_n = 0
for i in xrange(1,input()+1):
    if isSqFree(i):
        total_n += 1
        #print i,
#print ''
print total_n
