class Rectangle(object):
    def __init__(self,x,y,width,height):
        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height
    def overlapping(self, other):
        """
        overlapping(self, other) -> bool

        Check rectangle is overlapping if overlapping return True,
        Otherwise return False.
        """
        if (self.width+other.width)/2.0 > abs(self.x-other.x) and \
           (self.height+other.height)/2.0 > abs(self.y-other.y):
            return True
        return False

rec1 = Rectangle(*[input() for i in xrange(4)])
rec2 = Rectangle(*[input() for i in xrange(4)])

print ["no overlapping", "overlapping"][rec1.overlapping(rec2)]
