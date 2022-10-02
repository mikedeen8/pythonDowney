def ass_we_can():
    fin = open('words_folder/Billy_Herington.txt')
    demlimiter = '.'
    for line in fin:
        word = line.strip()
        t = word.split(demlimiter)
    print(t)

ass_we_can()