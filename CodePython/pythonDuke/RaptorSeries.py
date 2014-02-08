def d(ls):
    ls_new = []
    if sum(ls) == ls[0]*len(ls):
        return 0
    for i in xrange(1,len(ls)):
        ls_new.append(ls[i]-ls[i-1])
    print ls_new
    d(ls_new)

ls = []
total = 0
for i in xrange(1,input()+1):
    total += i*i
    ls.append(total)
print total
print ls
d(ls)
#n = input()
##print n*(n+1)*(2*n+1)/6
