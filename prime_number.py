# while True:
#     number = int(input('Enter a number: '))
#     if number > 1:
#         flag = True
#         for i in range(2, number):
#             if number % i == 0:
#                 flag = False

#         if flag:
#             print(f'The number {number} is Prime number')
#             break
#         else:
#             print(f'The number {number} is not a prime number')
#             break
#     else:
#         number = print('Enter a number greater than 1: ')

def isPrime(num):
    # while True:
        # num = int(input('Enter a number: '))
        if num > 1:
            flag = True
            for i in range(2, num):
                if num % i == 0:
                    flag = False
            if flag:
                print(f'{num} is Prime number')
                # break
            else:
                print('Not a Prime number')

        else:
            print('Enter a number greater than 1')

isPrime(11)
