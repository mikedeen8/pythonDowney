def ack(m, n):
    ## guardian 
    if not isinstance(m,  int) or not isinstance(n, int):
        print('m и n должны быть целыми числами')
    elif m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))
    else:
        print("m и n должны быть >= 0")

print(ack(4, 5))