def fabonacci(num):
    list = [0, 1]
    for i in range(num-2):
        list.append(list[-1] + list[-2])
    
    return list

print(fabonacci(10))