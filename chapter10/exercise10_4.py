def chop(t):
    del t[0]
    del t[-1]
    return 

t1 = [1, 2, 3, 4]
chop(t1)
print(t1)