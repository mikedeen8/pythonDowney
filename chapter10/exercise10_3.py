def middle(t):
    x = t[:]
    del x[0]
    del x[-1]
    return x

t1 = [1, 2, 3, 4, 'misha mraz', 'oleg mraz']
t2 = middle(t1)
print('t1:', t1, 't2:', t2)