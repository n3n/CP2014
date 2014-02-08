cnt_odd = 0
cnt_even = 0
for i in xrange(input()):
    n = input()
    if n % 2 == 0:
        cnt_even += 1
    else:
        cnt_odd += 1
print "%d\n%d" % (cnt_even, cnt_odd)
