from math import sqrt

def isPrime(n):
    if n == 1 or (n%2 == 0 and n != 2):
        return False
    for num in range(1, int(sqrt(n))+1, 2)[1:]:
        if n%num == 0:
            return False
    return True

def shiftNumLeft(n, step):
    return int(str(n)[step:] + str(n)[0:step])

def isCircularPrime(n):
    i = n
    set_n = set()
    for i_shift in xrange(len(str(n))):
        set_n.add(shiftNumLeft(n,i_shift))
    for num in list(set_n):
        if not isPrime(num):
            return False
    return True

n = input()
total = 0
for i in xrange(2,n+1):
    if isCircularPrime(i):
        total += i
print total
