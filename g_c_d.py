def gcd(num1, num2):
    m_list = []
    new_list = []

    for i in range(1, num1):
        if num1 % i == 0:
            m_list.append(i)

    for i in range(1, num2):
        if num2 % i == 0:
            m_list.append(i)

    for i in m_list:
        if m_list.count(i) == 2:
            new_list.append(i)

    new_list = list(set(new_list))

    if new_list:
        print(max(new_list))

gcd(555, 44)

    