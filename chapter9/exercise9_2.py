def has_no_e():
    x = input()
    if x.count('e') == 0:
        return True

# print(has_no_e())

fin = open('words_folder/words.txt')
x, y = 0, 0
for line in fin:
    word = line.strip()
    if word.count('e') == 0:
        x += 1
        print(word)
        # print(x)
    else:
        y += 1
        # print(y)
print(x / (y + x) * 100, '%')