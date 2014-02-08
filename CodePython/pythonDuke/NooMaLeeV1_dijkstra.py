def mycmp(a, b):
    return minimal[a[0]][a[1]] - minimal[b[0]][b[1]]

INF = 9999999999999999
row, column = input(), input()
ls = []
flat = []
minimal = []
for i in xrange(row):
    ls.append([])
    flat.append([])
    minimal.append([])
    for j in xrange(column):
        ls[i].append(input())
        flat[i].append(True)
        minimal[i].append(INF)

minimal[0][0] = 0
queue = [(0,0)]
n_queue = 1
flat[0][0] = False
while n_queue:
    cur = queue.pop(0)
    n_queue -= 1
    #print cur
    #print 'Queue:', queue
    if cur[0] > 0:
        if flat[cur[0]-1][cur[1]]:
            flat[cur[0]-1][cur[1]] = False
            queue.append((cur[0]-1, cur[1]))
            n_queue += 1
        minimal[cur[0]-1][cur[1]] = min(minimal[cur[0]-1][cur[1]], minimal[cur[0]][cur[1]]+ls[cur[0]-1][cur[1]])
    if cur[1] > 0:
        if flat[cur[0]][cur[1]-1]:
            flat[cur[0]][cur[1]-1] = False
            queue.append((cur[0], cur[1]-1))
            n_queue += 1
        minimal[cur[0]][cur[1]-1] = min(minimal[cur[0]][cur[1]-1], minimal[cur[0]][cur[1]]+ls[cur[0]][cur[1]-1])
    if cur[0] < row-1:
        if flat[cur[0]+1][cur[1]]:
            flat[cur[0]+1][cur[1]] = False
            queue.append((cur[0]+1, cur[1]))
            n_queue += 1
        minimal[cur[0]+1][cur[1]] = min(minimal[cur[0]+1][cur[1]], minimal[cur[0]][cur[1]]+ls[cur[0]+1][cur[1]])
    if cur[1] < column-1:
        if flat[cur[0]][cur[1]+1]:
            flat[cur[0]][cur[1]+1] = False
            queue.append((cur[0], cur[1]+1))
            n_queue += 1
        minimal[cur[0]][cur[1]+1] = min(minimal[cur[0]][cur[1]+1], minimal[cur[0]][cur[1]]+ls[cur[0]][cur[1]+1])
    queue.sort(cmp=mycmp)
    #for i in  xrange(row):
    #    print minimal[i]

print minimal[row-1][column-1]

#for i in  xrange(row):
#    print minimal[i]

#for i in  xrange(row):
#    print ls[i]
