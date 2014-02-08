n1, n2, n3 = [int(i) for i in raw_input()]
encryp = ''
for i in xrange(10):
    encryp += str((n1+i)%10+(n2+i)%10+(n3+i)%10)
print encryp
