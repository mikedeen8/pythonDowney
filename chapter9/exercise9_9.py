def is_palindrom(a):    
    return a == a[::-1]

def main():
    n = 0
    for i in range(10, 100):
        if is_palindrom(str(i) + str(i)[: : -1]) and i - int(str(i)[: : -1]) == 18:
            print(str(i), ' ', str(i)[: : -1])

print(main())

# print(str(73)[: : -1])

# print(int(str(13) + str(13)[: : -1]))