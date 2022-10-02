def check_fermat(a, b, c, n):
    if n > 2:
        if a != 0 and b != 0 and c != 0:
            if a ** n + b ** n == c ** n:
                print('Не может быть, Ферма ошибся!')
            else:
                print('Нет, это не работает:', a ** n, '+', b ** n, '!=', c ** n)
        else:
            print('Ошибка. Вы ввели число равное 0')
    else:
        print('Ты дурак что ли, эй?')

a = int(input('Введите целое число a:\n'))
b = int(input('Введите целое число b:\n'))
c = int(input('Введите целое число c:\n'))
n = int(input('Введите n(n должно быть больше 2!):\n'))  

check_fermat(a, b, c, n)