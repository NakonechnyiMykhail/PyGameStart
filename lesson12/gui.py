import turtle

def print_quad(pen, count): # count = 4 -> 1, 2, 3
    for quad in range(1, count+1):
        i = 0
        while i < 4:
            pen.forward(quad*50)
            pen.left(90)
            i += 1

t = turtle.Pen()

# print_quad(t, 4)
# t.reset() # clear all and go to start position
# print_quad(t, 3)
# t.clear()  # clear all
# print_quad(t, 2)

# t.backward(100)
# t.up()
# t.right(90)
# t.forward(20)
# t.left(90)
# t.down()
# t.forward(100)
i = 1
while i <= 4:
    t.forward(50)
    t.left(90)
    i += 1


turtle.mainloop()
