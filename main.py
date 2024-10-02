# num = input().split()
# print(type(num[0]))
# num = map(str, num)
# n_list = []
# for i in num:
#     if i.isdigit():
#         n_list.append(int(i))
#         print('Digit')
#     else:
#         n_list.append(str(i))

# print(n_list)

# from abc import ABC, abstractmethod

# class Animal():
#     @abstractmethod
#     def make_sound(self):
#         return 'OOOOwww'
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         return "Bark"

# class Cat(Animal):
#     def make_sound(self):
#         return "Meow"

# dog = Dog()
# cat = Cat()
# print(dog.make_sound())  # Output: Bark
# print(cat.make_sound())  # Output: Meow

# for i in range(1,101):
#     if i %3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# import heroes
# while True:
#     name = heroes.gen()
#     if name == "Spiderman":
#         print(f"Yes {name} is a Hero")
#         break
