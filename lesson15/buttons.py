from tkinter import *
# import turtle

def hello():
    print("hello")

def star1():
    import turtle

    t = turtle.Pen()

    for x in range(100):
        t.forward(100)
        t.left(60) # 95 / 105 / 80 / 70 / (60) 63/ (120) 125 / (144) 146

    turtle.mainloop()


def star2():
    import turtle

    t = turtle.Pen()

    for x in range(100):
        t.forward(100)
        t.left(120) # 95 / 105 / 80 / 70 / (60) 63/ (120) 125 / (144) 146

    turtle.mainloop()

def star3():
    import turtle

    t = turtle.Pen()

    for x in range(360):
        t.forward(1)
        t.left(1) # 95 / 105 / 80 / 70 / (60) 63/ (120) 125 / (144) 146

    turtle.mainloop()

def main():
    tk = Tk()
    tk.geometry('400x200')
    label = Label(tk, bg='green', text='MyBtn', font = ('arial', 40, 'bold'))
    label.place(x=0, y=0, width=400, height=200)

    btn = Button(tk, text="star1", font = ('arial', 20, 'bold'), command=star1)
    btn.place(x=25, y=125, width=100, height=25)

    btn2 = Button(tk, text="star2", font = ('arial', 20, 'bold'), command=star2)
    btn2.place(x=150, y=125, width=100, height=25)

    btn3 = Button(tk, text="star3", font = ('arial', 20, 'bold'), command=star3)
    btn3.place(x=275, y=125, width=100, height=25)

    #btn.pack()

    tk.mainloop()


if __name__ == '__main__':
    main()