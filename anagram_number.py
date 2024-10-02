# def anagram():
#     str1 = str(input('Enter a string: '))
#     str2 = str(input('Enter a string: '))

#     if sorted(str1) == sorted(str2):
#         print('The strings entered are anagram.')
    
#     else:
#         print('No')

# anagram()

dict_1 = {}
dict_2 = {}
str_1 = str(input())
str_2 = str(input())

for i in str_1:
    dict_1[i] = str_1.count(i)

for j in str_2:
    dict_2[j] = str_2.count(j)

if dict_1 == dict_2:
    print("anagram")

else:
    print("Not anagram")

print(dict_1)
print(dict_2)
