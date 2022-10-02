import math
def factorial(a):
    if a == 0 or a == 1:
        return 1
    elif a <= -1:
        return
    else:
        return a * factorial(a - 1)



def estimate_pi():
    first = 2 * math.sqrt(2) / 9801
    k = 0
    sum = 0
    second = 10
    while second > 1e-15:
        second = factorial(4 * k) * (1103 + 26390 * k) / ((factorial(k) ** 4) * 396 ** (4 * k))
        sum += first * second
        k = k + 1
    pi = 1 / sum
    return pi

print(estimate_pi())