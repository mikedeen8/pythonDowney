def is_palindrom(a):
    return a == a[::-1]

# print(is_palindrom('weeeew'))
        
        

# print(is_palindrom('ab' + 'ba'))
def create_list():
    fin = open('words_folder/words.txt')
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)

    return t


def is_para():
    i = 0
    t = create_list()
    fin = open('words_folder/words.txt')
    for w in fin:
        if w == w[::-1]:
            print(w, w[::-1])

print(is_para())
# print('asdfg'[::-1])