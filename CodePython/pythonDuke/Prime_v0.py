def isPrime(n):
    if n == 1:
        return False
    for num in range(2, n):
        if n%num == 0:
            return False
    return True

n = input()
print isPrime(n)
