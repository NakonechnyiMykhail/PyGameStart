#from sys import argv
import sys

# 1 part: print all arguments from new line
# for arg in argv:
#     print(arg)

# 2 part: if 2 args => print second arg
# if len(argv) == 2:
#     print(f"hello, {argv[1]}")
#     # print("hello,", argv[1])
# else:
#     print("hello, world")

# 3 part: check args and exit 
# if len(sys.argv) != 2:
#     print("missing command-line arguments")
#     sys.exit(1)
# print(f"hello, {sys.argv[1]}")
# sys.exit(0) 

## 4 part: search elements
# numbers = [0, 1, 4, 7, 9, 11, 15, 17, 22]
# ## get number from user
# # number = int(input('What number do you want to find? '))
# ## get number from command-line
# number = int(sys.argv[1])
# if number in numbers:
#     print("Found")
#     sys.exit(0)
# print("Not found")
# sys.exit(1) 

############################
names = ["Mike", "Ivan", "David", "Brian"]
## get name from user
# number = str(input('What name do you want to find? '))
## get number from command-line
name = str(sys.argv[1])
if name in names:
    print("Found")
    sys.exit(0)
print("Not found")
sys.exit(1) 
