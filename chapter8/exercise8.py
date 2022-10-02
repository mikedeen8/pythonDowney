def word():
    x = input()
    index = len(x) - 1
    while index >= 0:
        letter = x[index]
        print(letter)
        index = index - 1

print(word())