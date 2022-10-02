import math
def eval_loop():
    while True:
        a = input()
        if a == 'готово':
            print(b)
            break
        else:
            print(eval(a))
            b = eval(a)

eval_loop()