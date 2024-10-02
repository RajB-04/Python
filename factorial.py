inp = int(input())
def factorial(num):
    val = 1
    pattern = ''
    for i in range(num, 0, -1):
        val = val * i
        pattern += f'{i}*'
    pattern = pattern.strip('*')
    return f"{num}! = {pattern} = {val}"

factorial(inp) 

fact = factorial
get_list = list(map(fact, range(11)))
print(get_list)

# Lambda functions 
# inp = int(input())
# def multiply(x):
#     return lambda n: n * x
# m = multiply(inp)

# print(m(4))


# Dictionaries in python 

# lab = {
#     'name': 'Swami Vivekanand',
#     'librarian': 'Yuvraj Bhosale',
#     'books': 30000,
#     'place': 'Pune'
# }

# for i in list(lab.keys()):
#     if i == 'books':
#         lab['t_Books'] = 40000
# lab.pop('books')

# print(lab)



def fact(number):
    f = 1
    if number == 0 or number == 1:
        return 1
    else:
        f = number * fact(number-1)
        return f

print(fact(5))