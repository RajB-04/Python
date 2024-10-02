def palindrome():
    in_str = input('Enter a string: ')
    rev_str = in_str[-1::-1]

    if in_str == rev_str:
        print('The given string is a palindrome.')
    else:
        print('The given sring is not a palindrome')

palindrome()