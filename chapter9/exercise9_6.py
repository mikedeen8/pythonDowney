def is_abecedarian(word):
    n = 0
    while n < len(word) - 1:
        if word[n] > word[n + 1]:
            return False
        n += 1
    return True

def main():
    fin = open('words_folder/words.txt')
    m = 0
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            print(word)
            m += 1
    print(m)

main()