import random
def has_duplicates(t):
    for x in t:
        if t.count(x) > 1:
            return False
    return True

def generate_class():
    t = []
    n = 23
    for x in range(n):
        t.append(random.randint(1, 365))
    return t
    
def main():
    n_t = 0
    klass = 100
    for i in range(klass):
        if has_duplicates(generate_class()):
            n_t += 1
    print(n_t / klass * 100)

main()