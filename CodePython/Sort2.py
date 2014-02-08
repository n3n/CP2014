d = {}
while True:
    level, voltage = raw_input().split()
    if level == '0' and voltage == '0':
        choice = raw_input().lower()
        break
    d[int(level)] = float(voltage)
if choice == 'min':
    select = True
else:
    select = False
for i in sorted(d, key=d.get, reverse=select):
        print i,'%.4f' % d.get(i)
