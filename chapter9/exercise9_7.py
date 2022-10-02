def double_letter(word):
    n = 0
    while n < len(word) - 1:
        if len(word) - 1 - n >= 5:
            if word[n] == word[n + 1] and word[n + 2] == word[n + 3] and word[n + 4] == word[n + 5]:
                return True
        n += 1

    return False

# print(double_letter(input()))


def main():
    fin = open('words_folder/words.txt')
    m = 0
    for line in fin:
        word = line.strip()
        if double_letter(word):
            print(word)

main()