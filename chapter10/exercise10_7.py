def has_duplicates(t):
    for x in t:
        if t.count(x) > 1:
            return False
    return True

print(has_duplicates([1, 2, 3, 4, 5, 'm', 'r', 'a', 'z', 'misha']))