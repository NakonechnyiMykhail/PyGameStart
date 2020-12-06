import turtle

t = turtle.Pen()


#     /\
#    /  \
#   /    \
#  /______\

# i = 0
# while i < 3:
#     t.forward(50)
#     t.left(120)
#     i += 1

# left/right =>
# 120 - треугольник
# 90  - квадрат
# 60  - шестиугольник 
# 45  - восьмиугольник
# 30  - двенадцатиугольник
# ..  - круг
#

i = 0
while i < 6: # количество сторон
    t.forward(40) # количество "шагов" в направлении ...
    t.left(60) # поворот на угол 60 влево от основного направления
    i += 1 


# t.reset()

# for x in range(36):
#     t.forward(20)
#     t.left(10) 

# i = 0
# while i < 3:
#     t.forward(50)
#     t.left(120)
#     i += 1

# t.reset()

# #3

# t.reset()

# #4
# t.reset()

turtle.mainloop()