def greater(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None
    
result = greater(10, 10)

print(result)