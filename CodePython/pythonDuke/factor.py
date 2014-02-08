def primeToNumber(n):
    n += 1
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]
    
def primeToNumberA(n):
    table = [i for i in xrange(n+1)]
    for i in xrange(2, int(n**0.5)+1):
        if table[i]:
            for mult in range(i**2, n+1, i):
                table[mult] = False
    return [p for p in table if p][1:]

def is_prime(n):
    for i in xrange(2, n):
        if n%i == 0:
            return False
    return True
    
n = input()
#prime = primeToNumber(n)
print 'aa'
#print prime
#st = str(n) + ' = ' 
#for p in prime:
#    while n%p == 0:
#        st += (str(p) + ' x ')
#        n /= p
#print st[:-2]

#st = str(n) + ' = '
#for i in xrange(2,n+1):
#    if is_prime(i):
#        while n%i == 0:
#            st += (str(i) + ' x ')
#            n /= i
#print st[:-2]
