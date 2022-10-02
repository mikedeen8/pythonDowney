def uses_all(word, sub):
    for s in sub:
        if not s in word:
            return False

    return True
        

def main():
    fin = open('words_folder/words.txt')
    sub = input("Что это за слово?\n")
    for line in fin:
        word = line.strip()
        if uses_all(word, sub):
            print(word)

main()