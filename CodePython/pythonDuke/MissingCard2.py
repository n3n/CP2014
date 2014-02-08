def my_cmp(a, b):
    typ = '23456789TJQKA'
    rnk = 'CDHS'
    if typ.index(a[0]) - typ.index(b[0]) == 0:
        return rnk.index(a[1]) - rnk.index(b[1])
    return typ.index(a[0]) - typ.index(b[0])

deck = {}
for i in '23456789TJQKA':
    for j in 'CDHS':
        deck[i+j] = False

for i in range(input()):
    deck[raw_input()] = True

result = []
for i in deck:
    if deck[i] == False:
        result.append(i)

result.sort(cmp=my_cmp)
for i in result:
    print i
