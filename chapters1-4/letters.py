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

def draw_a(t, h):
    """
    draw a letter A with height h
    """
    t.lt(75)
    l = h/math.cos(15*math.pi/180)
    t.fd(l)
    t.rt(150)
    t.fd(l)
    t.bk(l/3)
    t.rt(105)
    t.fd(4/3*l*math.sin(15*math.pi/180))
    t.pu()
    t.bk(4/3*l*math.sin(15*math.pi/180))
    t.lt(105)
    t.fd(l/3)
    t.lt(75)
    t.pd()

def draw_z(t, h):
    """
    draw a letter Z with height h
    """
    l = h/math.cos(15*math.pi/180)
    t.fd(l)
    t.rt(135)
    t.fd(l*2/math.sqrt(2))
    t.lt(135)
    t.fd(l)

def draw_y(t,h):
    """
    draw a letter Y with height h
    """
    l = h/math.cos(15*math.pi/180)
    t.lt(90)
    t.fd(l)
    t.lt(45)
    t.fd(l)
    t.rt(180)
    t.fd(l)
    t.lt(90)
    t.fd(l)
    t.rt(180)
    t.fd(l)
    t.lt(45)
    t.fd(l)
    t.lt(90)
    
def draw_x(t, h):
    """
    draw a letter X with height h
    """
    l = h/math.cos(15*math.pi/180)
    t.rt(45)
    t.fd(l)
    t.pu()
    t.lt(135)
    t.fd(math.sqrt((l**2/2)))
    t.pd()
    t.lt(135)
    t.fd(l)
    t.pu()
    t.lt(135)
    t.fd(math.sqrt((l**2/2)))

def draw_w(t, h):
    """
    draw a letter W with height h
    """
    l = h/math.cos(15*math.pi/100)
    t.pu()
    t.lt(90)
    t.fd(l)
    t.pd()
    t.rt(160)
    t.fd(l)
    t.lt(5)
    t.fd(l)

def draw_u(t, h, r, angle):
    l = h/math.cos(15*math.pi/100)
    t.rt(45)
    arc(t, r, angle)
    t.lt(45)
    t.fd(l)
    t.lt(90)
    t.pu()
    t.fd(2*math.pi*r/360*angle)
    t.lt(90)
    t.pd()
    t.fd(l)


Billy = turtle.Turtle()

draw_u(Billy, 100, 100, 90)

turtle.mainloop()