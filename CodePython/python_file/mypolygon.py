from swampy.TurtleWorld import *
from math import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.00000000000000000001
def square(t, length):
    for i in range(4):
        fd(t,length)
        lt(t)

def polygon(t, l, n):
    for i in range(4):
        fd(t, l)
        lt(t, n)

def circle(t, r, length, n):
	for i in range(n):
		lt(bob, r)
		fd(bob, length)
	wait_for_user()

'''def circle(t,r):
    circumference = 2 * pi * r
    n = 500
    length = circumference / n
    polygon(t,n,length)'''

'''def polygon(t, n, l):
    angle = 360.0/n
    for i in range(n):
        fd(t, l)
        lt(t, angle)
    wait_for_user()
'''
#r = input("Radius : ")
l = input("length : ")
n = input("Round : ")

#circle(bob, r, l, n)
polygon(bob, l, n)
