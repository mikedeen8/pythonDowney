def cumsum(t):
    total = 0
    s = []
    for x in t:
        total += x
        s.append(total)
    return s

print(cumsum([1, 2, 3, 4]))