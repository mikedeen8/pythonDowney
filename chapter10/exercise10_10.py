# r = 0
# def count():
#     global r
#     if print(count()) > 100:
#         return
#     r += 1
#     return r

# def return_none():
#     pass
r = 0
def count():
    global r
    if r == 100:
        return True
    else:
        r += 1

# print(return_none())

def in_bisect(w, t):
    # global r
    # if r is None:
    #     return
    # else:
    #     if r != 100:
    #         r += 1
    #         print(r)
    #     else:
    #         return
    index = 0
    #naiti mid
    mid = len(t) // 2
    x = t[mid]
    #sravnit w s mid elementom iz t    
    if x > w:
        # print(len(t[index:]))
        print(index)   
        return index + in_bisect(w, t[:mid])
    #esli menche return index + inbisect() oraninict t otrezat vtoruyu polovinu
    elif x < w:
        index += mid
        print(index)
        # print(len(t) - index)
        # print(len(t[index:]))
        # print(index)
        return index + in_bisect(w, t[mid:])
    #elsi w bolshe index += mid; return index + inbisect t obrazat perbuyu polovine
    elif x == w:
        return index + mid  
    #esli w == tmid retrun index + mid
    #pishi mraz

def create_list():
    fin = open('words_folder/words.txt')
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)

    return t

def main():
    txt = create_list()
    word = 'wwew'
    #print(txt[0])
    print(in_bisect(word, txt))

main()
# print('qwerty'[1])
# print('0' < 'a')
# s = [1, 2, 3, 4, 5]
# print(s[1])
# print(s)
