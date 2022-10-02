from tkinter import Y


def rotate_word():
    a = input('Enter word:\n')
    b = int(input('enter shift number:\n'))
    x = ''
    for i in a:
        y = chr(ord(i) + b)
        x += y
    print(x)

rotate_word()