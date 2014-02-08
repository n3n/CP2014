n = input()
k = input()
fibo_used = [[] for i in xrange(n+5)]
fibo_used[0].append(1)
fibo_used[1].extend([0,1])

for i in xrange(2,n+1):
    for j in xrange(i-1):
        fibo_used[i].append(fibo_used[i-1][j] + fibo_used[i-2][j])
    fibo_used[i].append(fibo_used[i-1][i-1])
    fibo_used[i].append(1)

#for i in xrange(n+1):
#    print i, fibo_used[i]
print fibo_used[n][k]
