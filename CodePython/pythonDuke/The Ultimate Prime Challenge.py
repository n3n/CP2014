from time import time 
from math import floor

def isPrimeV1(n):
    n_sqrt = n**0.5
    for prime in primes:
        if prime > n_sqrt:
            break
        elif n%prime == 0:
            return False
    return True

def isPrime(n):
    n_sqrt = n**0.5
    if floor(n_sqrt) == n_sqrt:
        return False
    for prime in primes:
        if prime > n_sqrt:
            break
        elif n%prime == 0:
            return False
    return True

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def primes_sieve3(limit):
    limit = [limit+1, 3][limit < 2]
    n_table = [True] * limit
    n_table[0] = n_table[1] = False
    limit_sqrt = int(limit**0.5)+1
    for i in xrange(2, limit_sqrt):
        if n_table[i]:
            for n in xrange(i*i, limit, i):
                n_table[n] = False
    return n_table.count(True)

def count(g):
    cnt = 0
    try:
        for i in g:
            cnt += 1
    except:
        print 'Error at', i
    return cnt

n = input()
t = time()
#primes = [[],[2]][n>=2]
#for i in xrange(3, n+2, 2):
#    if isPrime(i):
#        primes.append(i)
#print len(primes)
#print count(primes_sieve2(n))
print primes_sieve3(n)
print 'total times: ' + str(time() - t)
