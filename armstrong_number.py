def armstrong_number():
    num = int(input())
    s_num = str(num)    
    a_sum = 0

    for j in s_num:
        m = int(j)
        a_sum += m*m*m

    if num == a_sum:
        print(f'The number {num} is a armstrong number.')
    else:
        print(f'The number {num} is  not a armstrong number.')


armstrong_number()
