import time 
def word_list():
    fin = open('words_folder/words.txt')
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)


def word_list_2():
    fin = open('words_folder/words.txt')
    t = []
    for line in fin:
        word = line.strip()
        t = t + [word]

def main():
    start1 = time.time()
    word_list()
    end1 = time.time()
    start2 = time.time()
    word_list_2()
    end2 = time.time()

    print("t1", end1 - start1, "t2", end2 - start2)

main()
