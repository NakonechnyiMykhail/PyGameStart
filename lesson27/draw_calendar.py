from tkinter import *
import calendar

root = Tk()
root.title('Own Calendar')

year = 2021
myCal = calendar.calendar(year)

#print(myCal) # at terminal

cal_year = Label(root, text=myCal, font="Consolas 12 bold")
cal_year.pack()
root.mainloop()