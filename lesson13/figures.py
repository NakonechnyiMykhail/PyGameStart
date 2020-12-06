import turtle

t = turtle.Pen()

i = 0 # 3 * 120 = 360
while i < 3:
    t.forward(50)
    t.left(120) 
    i += 1

t.reset()

i = 0 # 4 * 90 = 360
while i < 4:
    t.forward(50)
    t.left(90)
    i += 1

t.reset()

i = 0 # 6 * 60 = 360
while i < 6:
    t.forward(25)
    t.left(60) 
    i += 1

t.reset()

i = 0 # 8 * 45 = 360
while i < 8:
    t.forward(25)
    t.left(45) 
    i += 1

t.reset()

i = 0 # 12 * 30 = 360
while i < 12: 
    t.forward(25)
    t.left(30) 
    i += 1

t.reset()

i = 0 # 36 * 10 = 360 OR 360 * 1 = 360
while i < 360:
    t.forward(2)
    t.left(1) 
    i += 1

# t.reset()


turtle.mainloop()