li = [1, 3, 4, 5, 7, 22, 11] # our list 
li_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] #...
li_chars2 = 'a b c d e f g h i j k l m n o p'.split()

li2 = ['Mike', 22, 'Kharkiv', '+38(099)-999-99-99']

# task:
# a
# b
# c
# d
# e
# f
# ...

# python loops: while, for

# while ...:
#     print()

# range(10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for index in li_chars2:
#     print(index)
# print('\n'.join(li_chars2))
# print('\n'.join(li))
# print(li)

# code loop:
#    print()

def hello(str1:str, str2:str, age:int):
    """
    function PRINT greet

    parameters:
        - str1 = user name
        - str2 = user surname
        - age  = user age
    """
    print(str1,str2, age)

for index in range(10):
    hello("Mike", "Nik", 12)


# # range(10) 
# li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(li)
# for index in li:
#     print(index)

# li2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print_list(li2)

# li3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(li3)
# for index in li3:
#     print(index)

# li4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(li4)
# for index in li4:
#     print(index)
