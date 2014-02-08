n = input()
stirling_num = [[0] for i in xrange(n+1)]
stirling_num[0][0] = 1

for row in xrange(1,n+1):
    for k in xrange(1,row):
        stirling_num[row].append(k*stirling_num[row-1][k] + stirling_num[row-1][k-1])
    stirling_num[row].append(1)
    
print sum(stirling_num[n])
