def f(n):
    if n == 1:
        return 1
        pass
    if n%2 == 0:
        if not value.has_key(n/2):
            value[n] = f(n/2) + 1
        else:
            value[n] = value[n/2] + 1 
    else:
        if not value.has_key(n*3+1):
            value[n] = f(n*3+1) + 1
        else:
            value[n] = value[n*3+1] + 1
        #value[n] = t + 1
    return value[n]

value = {1:1}
for i in xrange(input(), 1, -1):
    f(i)
print max(value.values())
