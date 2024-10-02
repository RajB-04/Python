str = input('Enter a string:' )
flag = False
for s in str:
    if s.isalnum():
        flag = True
        break 
print(flag)

flag = False
for s in str:
    if s.isalpha():
        flag = True
        break
print(flag)

flag = False
for s in str:
    if s.isdigit():
        flag = True
        break
print(flag)

flag = False
for s in str:
    if s.islower():
        flag = True
        break
print(flag)

flag = False
for s in str:
    if s.upper():
        flag = True
        break
print(flag)
