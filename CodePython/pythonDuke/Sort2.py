ls = []
t = (-1,-1)
while t != (0,0):
    t = tuple(map(float, raw_input().split())[-1::-1])
    ls.append(t)
ls = ls[:-1]
cmd = raw_input().lower()

if cmd == 'max':
    ls.sort()
else:
    ls.sort(reverse=True)

for v,f in ls:
    print int(f), [int(v), '%.4f'%v][v!=int(v)]
