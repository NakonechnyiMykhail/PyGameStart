import tkinter as tk
from tkinter import ttk
import sys
from random import randrange

FONT_SIZE = (24, 26, 28, 30, 32, 36, 40, 42, 44, 50, 56, 65, 72, 76, 78)
DEFAULT_SIZE = 46
NUMBER_OF_FONTS = len(FONT_SIZE)
FONT = ("Verdana", DEFAULT_SIZE)
LETTERS_BOTTOM_RUS = ('О', 'Л', 'П')
LETTERS_BOTTOM_ENG = ('R', 'L', 'B')
# https://www.w3schools.com/colors/colors_picker.asp
COLORS = (
    "#563093", # purple
    "#911414", # red
    "#cec379", 
    "#B76EFF", 
    "#FF90FF",
    "#9CFF9C", 
    "#FFB76E", 
    "#A3A375", 
    "#9F9FFF", 
    "#FF66CC")
NUMBER_OF_COLORS = len(COLORS)

class AlphabetGame(tk.Toplevel):

    def __init__(self, original_frame, lang, random_order, change_pos, 
                change_font_size, change_color, pause):
        tk.Toplevel.__init__(self)
        self.original_frame = original_frame
        self.lang = lang
        self.pause = pause
        self.protocol("WM_DELETE_WINDOW", sys.exit)
        # set window size 
        w = 800 # width
        h = 650 # height
        # ws = width_size / hs = height_size
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        # calculate window pos -> set center on screen
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.title("Alphabet")
        self.configure(background='white')

        self.canvas = tk.Canvas(self)
        self.canvas.grid()
        self.canvas.configure(background='white', width=800, height=600)

        btn = ttk.Button(self, text="Back", command=self.close_back_to_settings)
        btn.grid()
