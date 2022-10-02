def is_sorted(t):
    x = t[:]
    x.sort()
    print(x)
    return x == t
    
print(is_sorted(['1', 'a', 'm', 'r', 'a', 'z']))

# t = [1, 5, 3, 4]
# x = t[:]
# x.sort()
# print(x, t)