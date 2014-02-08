def fibo(n):
    fibo_num = [1,1]
    for i in xrange(2,n+1):
        fibo_num.append(fibo_num[i-1]+fibo_num[i-2])
    return fibo_num[n]

n = input()
k = input()
div = n-k

if k == 0:
    div -= 2

if div - 1 < 0:
    print 1
else:
    print fibo(div)
