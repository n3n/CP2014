n   = input()
pos = input()-1
k   = input()-1
ls  = [i for i in xrange(1,n+1)]

for i in xrange(n, 1, -1):
    pos = (pos+k)%i
    ls.pop(pos)
    
print ls[0]
