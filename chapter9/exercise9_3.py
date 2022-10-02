def avoids():
    word = input()
    b = input()
    return word.count(b) == 0

def avoids_words():
    forbidden = input('Введите запрещённую(-ые) быкву(-ы):\n')
    fin = open('words_folder/words.txt')
    n = 0 # kol-vo slov bez zapretnix
    for line in fin:
        word = line.strip()
        n_f = 0 # d
        for f in forbidden:
            n_f += word.count(f) 
        #esli otsutstvuyut
        if n_f == 0:
            n += 1   
            print(word) 
    print('Количество мразей-слов:', n)
        
avoids_words()