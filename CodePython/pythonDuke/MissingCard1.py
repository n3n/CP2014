deck = {}
for i in '23456789TJQKA':
    for j in 'CDHS':
        deck[i+j] = False

for i in range(51):
    deck[raw_input()] = True

print deck.keys()[deck.values().index(False)]
