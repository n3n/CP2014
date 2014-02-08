from math import sqrt

def isPrime(n):
    if n == 1 or (n%2 == 0 and n != 2):
        return False
    for num in range(1, int(sqrt(n))+2, 2)[1:]:
        if n%num == 0:
            return False
    return True

n = input()
total = 0
for i in range(1, n+1):
    if isPrime(i):
        total += 1
        #print i
print total
