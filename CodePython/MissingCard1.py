def gen_Card():
	level = '23456789TJQKA'
	rank = 'CDHS'
	card = []
	for i in level:
		for j in rank:
			card.append(i+j)
	return card
	
print gen_Card()


def MissingCard1():
	deck = gen_Card()
	for i in xrange(51):
		deck.remove(raw_input())
	return deck[0]
#print MissingCard1()


def MissingCard2():
	deck = gen_Card()
	for i in xrange(input()):
		deck.remove(raw_input())
	for j in deck:
		print j
	
#MissingCard2()
