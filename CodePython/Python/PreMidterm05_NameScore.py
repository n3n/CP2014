# ตามนั้น ขี้เกียจพิมพ์
test = input()
for case in xrange(test):
	name = raw_input()
	score = 0
	for letter in name:
		score += ord(letter) - 64
	print 'Name', case + 1,':', (case + 1 )* score