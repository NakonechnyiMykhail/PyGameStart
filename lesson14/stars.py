import turtle

t = turtle.Pen()

def drawStar(n, l):
    """
    n - размер звезды
    l - количество "шагов"
    """
    turtle.color("red", "green")
    turtle.begin_fill()
    for x in range(n):
        turtle.forward(l)
        turtle.left(2 * 360 / n)
    turtle.end_fill()

drawStar(32, 100)

# for x in range(9):
#     t.forward(100)
#     t.left(225)

# for x in range(5):
#     t.forward(100)
#     t.right(144)

# for x in range(100):
#     t.forward(100)
#     t.left(115) # 95 / 105 / 80 / 70 / (60) 63/ (120) 125 / (144) 146

#turtle.exitonclick()
turtle.mainloop()