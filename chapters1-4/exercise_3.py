from tkinter import mainloop
import turtle
import math

def triygolnik(t, r, alpha):
    beta = (180 - alpha)/2
    l = 2*r*math.sin(alpha/2*math.pi/180)
    t.rt(alpha/2)
    t.fd(r)
    t.lt(180 - beta)
    t.fd(l)
    t.lt(180 - beta)
    t.fd(r)
    t.lt(180 - alpha/2)

def pyat(t, r, n):
    gamma = 360 / n
    for i in range(n):
        triygolnik(t, r, gamma) 
        t.lt(gamma)

lalka = turtle.Turtle()
# triygolnik(lalka, 100, 60)
pyat(lalka, 100, 7)
lalka.hideturtle()

turtle.mainloop()
