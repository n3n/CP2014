def sum_divisor(n):
    if n == 1:
        return 0
    total_divisor = 1
    i = 2
    rootn = n**0.5
    while i < rootn:
        if n%i == 0:
            total_divisor += i + n/i
        i += 1
    if rootn == i:
        total_divisor += rootn
    return total_divisor

for i in xrange(input()):
    print sum_divisor(input())
