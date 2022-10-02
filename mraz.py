def do_twice(f):
    f()
    f()
def print_spam():

    print('Спам')

    do_twice(print_spam)