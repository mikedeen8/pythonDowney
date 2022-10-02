def is_palindrom(a):    
    return a == a[::-1]

def is_palindrom_i():
    for i in range(0, 999999):
        l = len(str(i))
        if l == 6 and is_palindrom(str(i)[-4 : ]) and is_palindrom(str(i + 1)[-5 : ]) and is_palindrom(str(i + 2)[1 : 5]) and is_palindrom(str(i + 3)[-6 : ]):
            print(i)

is_palindrom_i()

# print('123456'[1 : 5])