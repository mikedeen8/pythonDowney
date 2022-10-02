import turtle

def Koch(t, x, n):
    # n - количество уровней
    if n == 0:
        t.fd(x)
        return
    Koch(t, x/3, n - 1)
    t.lt(60)
    Koch(t, x/3, n - 1)
    t.rt(120)
    Koch(t, x/3, n - 1)
    t.lt(60)
    Koch(t, x/3, n - 1)

mraz = turtle.Turtle()
mraz.pu()
mraz.bk(500)
mraz.pd()
Koch(mraz, 900, 6)
turtle.mainloop()