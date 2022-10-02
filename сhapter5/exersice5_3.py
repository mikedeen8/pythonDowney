from operator import is_


def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print('Да')
    elif a + b == c or a + c == b or b + c == a:
        print('Вырожденный треугольник')
    else:
        print('Нет')

a = int(input('Введите  a:\n'))
b = int(input('Введите  b:\n'))
c = int(input('Введите  c:\n'))

is_triangle(a, b, c)
