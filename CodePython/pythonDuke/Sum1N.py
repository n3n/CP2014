n = input()
total = 0
if n > 1:
    for i in xrange(n, 0, -1):
        total += i
else:
    for i in xrange(n, 2, 1):
        total += i
print total
