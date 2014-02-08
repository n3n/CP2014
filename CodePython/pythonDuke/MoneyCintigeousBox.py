n = input()
ls = [input() for i in xrange(n)]
money_max = 0
for i_head in xrange(n):
    total = 0
    for i_rear in xrange(i_head, n):
        total += ls[i_rear]
        if total < 0:
            break
        money_max = max(total, money_max)
print money_max
