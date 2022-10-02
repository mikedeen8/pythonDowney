import math


def mysqrt(a):
   x = a / 1.5 
   while True:
    y = (x + a / x) / 2
    if y == x:
        break
    x = y
    return x


# print(mysqrt(1024))

def test_square_root():
    print('a    mysqrt(a)   math.sqrt(a)    diff')
    print('-    ---------   ------------    ----')
    a = 1.0
    i = 1
    while i != 10:
        # print(a, '', round(mysqrt(a), 10),'      ',  round(math.sqrt(a), 10), ' ', round(abs(math.sqrt(a) - mysqrt(a)), 10))
        print("{:.2f}    {:.5f}   {:.5f}    {:.5f}".format(a, mysqrt(a), math.sqrt(a), abs(math.sqrt(a) - mysqrt(a))))
        a += 1.0
        i += 1  
        
test_square_root()