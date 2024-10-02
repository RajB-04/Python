# for i in range(5):
#     print(f"{(i+1)*'*  '}")

# def pyramid(n):
#     for i in range(n):
#         print(f"{(n-i+1)*" "}{(i+1) * '* '}")

# pyramid(5)


num = 1
for i in range(0, 5):
    for j in range(0, i+1):
        print(f"{(num)}  ", end='')
        num += 1
    print()



