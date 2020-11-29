import turtle

t = turtle.Pen()
i = 0
# while i <= 4:
#     t.forward(50)
#     t.up()
#     t.forward(50)
#     t.down()
#     t.left(90)

#     i += 1
#|      -----
#|           
#|          
#           |
#           |
# ____      |


# HOMEWORK
# while i < 4:
#     t.up()
#     t.forward(30)
#     t.down()
#     t.forward(60)
#     t.up()
#     t.forward(30)
#     t.left(90)
#     i += 1


while i < 4:
    t.down()
    t.forward(30)
    t.up()
    t.forward(60)
    t.down()
    t.forward(30)
    t.left(90)

    i += 1



turtle.mainloop()