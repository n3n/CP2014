def fibo(n):
    f[n] += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

n = input()
f = [0 for i in xrange(n+1)]
fibo(n)
print f[input()]
