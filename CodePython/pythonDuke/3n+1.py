def f(n, each):
    if n == 1:
        return each
    elif n%2 == 0:
        return f(n/2, each+1)
    return f(n*3+1, each+1)

n = -1
total = 0
while n != 0:
    n = input()
    if n != 0:
        print f(n, 1)
