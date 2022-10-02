prefixes = 'БВККЛМНШ'
suffix = 'ряк'
for letter in prefixes:
    if letter == 'Л' or letter == 'М' or letter == 'Н':
        print(letter + 'як')
    elif letter == prefixes[3]:
        print(letter + 'вяк')
    else:
        print(letter + suffix)
