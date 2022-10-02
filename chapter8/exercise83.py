def find(word, letter, d):
    c = word[d: ]
    index = 0
    while index < len(c):
        if c[index] == letter:
            return index
        index = index + 1
    return -1


def count():
    a = input()
    b = input()
    count = 0
    for letter in a:
        if letter == b:
            count = count + 1
    print(count)

print(count())