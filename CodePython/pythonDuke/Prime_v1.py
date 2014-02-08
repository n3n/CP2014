from math import sqrt

def isPrime(n):
    if n == 1:
        return False
    for num in range(1, int(sqrt(n)), 2)[1:]:
        if n%num == 0:
            return False
    return True

n = input()
print isPrime(n)
