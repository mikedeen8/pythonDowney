def add_all(t):
    total = 0
    for x in t:
        total += x
        
    return total

# def nested_sum(y):
#     total_1 = 0
#     for s in y:
#         total_1 += add_all(s)
#     return total_1
    
def nested_sum(t):
    sum = 0
    for x in t:
        if type(x) == list:
            sum += nested_sum(x)
        else: 
            sum += x
    return sum

print(type([1, 2, 3]))
print(nested_sum([[1, 2, 3], [3], [[4, 5, 6], [3, 6, 5]]]))
