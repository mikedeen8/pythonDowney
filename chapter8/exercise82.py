def find(word, letter, d):
    c = word[d: ]
    index = 0
    while index < len(c):
        if c[index] == letter:
            return index
        index = index + 1
    return -1

print(find('mraz', 'z', 1))