import turtle
import math


def arc(t, r, angle):
    arclength = 2*math.pi*r/360*angle
    n = int(arclength / 3) + 1
    length = arclength/n
    polyline(t, n, length, angle/n)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    
def petal(t, l, r):
    beta = math.acos(1 - l**2/(2*r**2))*180/math.pi
    alpha = 90 - beta/2
    t.lt(alpha)
    arc(t, r, beta)
    t.lt(180-beta)
    arc(t, r, beta)
    t.lt(alpha)

def flower(t, n, l, r):
    for i in range(n):
        gamma = 360 / n
        t.lt(gamma)
        petal(mraz, l, r)


mraz = turtle.Turtle()

flower(mraz, 7, 100, 100)

# petal(mraz, 100, 100)

turtle.mainloop()