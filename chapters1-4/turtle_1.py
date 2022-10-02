# функция square для turtle
import turtle
import math

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    polyline(t, n, length, 360/n)

def circle(t, r):
    # circumference = 2*math.pi*r
    # n = int(circumference / 3) + 1
    # length = circumference / n
    # polygon(t, length, n)
    arc(t, r, 360)

def arc(t, r, angle):
    arclength = 2*math.pi*r/360*angle
    n = int(arclength / 3) + 1
    length = arclength/n
    polyline(t, n, length, angle/n)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

mraz = turtle.Turtle()

arc(mraz, 100, 45)

# circle(mraz, 10)
# circle(mraz, 20)
# circle(mraz, 30)
# circle(mraz, 40)
# circle(mraz, 50)

# polygon(mraz, 0.1, 1000)

# square(mraz, 250)

turtle.mainloop()