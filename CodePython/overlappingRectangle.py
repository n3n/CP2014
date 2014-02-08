class Rectangle(object):
    '''
    Class of rectangle
    '''
    def dist(x1, y1, x2, y2):
	return int((((x1 - x2) **2)+ ((y1 - y2) ** 2)) ** 0.5)
    

x1, y1, w1, h1 = input(), input(), input(), input()
x2, y2, w2, h2 = input(), input(), input(), input()
