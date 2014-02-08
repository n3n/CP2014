m, n = input(), input()
ls = []
minimal = []
for i in range(m):
    ls.append([])
    minimal.append([])
    for j in range(n):
        ls[i].append(input())
        minimal[i].append(-1)
        if i > 0 and j > 0:
            minimal[i][j] = min(ls[i][j] + minimal[i][j-1], ls[i][j] + minimal[i-1][j])
        elif i == 0 and j > 0:
            minimal[i][j] = ls[i][j] + minimal[i][j-1]
        elif i > 0 and j == 0:
            minimal[i][j] = ls[i][j] + minimal[i-1][j]
        else:
            minimal[i][j] = 0
print minimal[m-1][n-1]

for i in xrange(m):
    print minimal[i]
