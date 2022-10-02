def is_anagram(a ,b):
    t = list(a)
    x = list(b)
    t.sort()
    x.sort()
    return t == x

print(is_anagram('Ass We Can', 'As We scan'))