from tkinter import *
#from PIL import Image, ImageTk # jpg

def start():
    print("start")


def reset():
    print("reset")


def settings():
    print("settings")


def exit():
    print("exit")

root = Tk()

root.geometry("500x500")
bg = PhotoImage(file="space1.png") # PNG
#load = Image.open("space.jpg")
#render = ImageTk.PhotoImage(load)
img = Label(root, image=bg)
img.image = bg
img.place(x=0, y=0)

lbl = Label(root, text="Welcome", bg="#fff000")
lbl.pack(pady=50)

# frame = Frame(root, bg="#ffffff") # #000000 = black color
# frame.pack(pady=20)

# center 
# x - ??? 
# geometry_width = 500 -> / 2 -> 250
# button_width = 100 -> /2 -> 50
# center_x = geometry_width - button_width = 200

btn1 = Button(root, text="Start", bg='brown', fg='green', font=('times', 20, 'bold'), command=start)  # root -> frame
btn1.place(x=200, y=100, width=100, height=25)
#btn1.pack(pady=20)


btn2 = Button(root, text="Reset", bg='brown', fg='green', font=('times', 20, 'bold'), command=reset)  # root -> frame
btn2.place(x=200, y=150, width=100, height=25)
#btn2.pack(pady=20)

btn3 = Button(root, text="Settings", bg='brown', fg='green', font=('times', 20, 'bold'), command=settings)  # root -> frame
btn3.place(x=200, y=200, width=100, height=25)
#btn3.pack(pady=20)

btn4 = Button(root, text="Exit", bg='brown', fg='green', font=('times', 20, 'bold'), command=exit)  # root -> frame
btn4.place(x=200, y=250, width=100, height=25)
#btn4.pack(pady=20)



root.mainloop()
