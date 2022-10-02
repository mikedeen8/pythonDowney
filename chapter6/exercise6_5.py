def gcd(a, b):
    #базовый случай:gcd(a , 0)
    # В этом случае gcd(a, b) -> a = a, b = 0 
    if b == 0:
        return a 
    else: 
        return gcd(b, a % b) # Я Миша, Я тупая мразь

print(gcd(1024, 1000))
