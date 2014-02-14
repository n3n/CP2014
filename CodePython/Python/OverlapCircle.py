def dist(x1, y1, x2, y2):
	return int(abs((abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2)) ** 0.5)

x1 = input()
y1 = input()
r1 = input()
x2 = input()
y2 = input()
r2 = input()

di = dist(x1, y1, x2, y2)
if di < r1 + r2:
	print 'overlapping'
else:
	print 'no overlapping'