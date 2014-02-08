def ceilling(n):
    if int(n) != n:
        return int(n) + 1
    return int(n)

n, k = map(int, raw_input().split())
ls = [i for i in xrange(2, n+1)]
prime = 2

trigger = True
while trigger:
    trigger = False
    for num in ls:
        if num%prime == 0:
            k -= 1
            if k == 0:
                print num
                trigger = False
                break
            ls.remove(num)
            trigger = True
    if ls and trigger:
        prime = ls[0]
