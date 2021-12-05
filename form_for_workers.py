import tkinter as tk
from tkinter import Tk, RIGHT, BOTH, RAISED, LEFT, Y, TOP


class Example(tk.Frame):
    def __init__(self, parent, restoraunt):
        super().__init__(parent)

        self.parent = parent
        self.restoraunt = restoraunt
        self.init_ui()

    def init_ui(self):
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side=LEFT)

        self.submenu_frame = tk.Frame(self)
        self.submenu_frame.pack(side=TOP)


        self.pack()

    # def on_click(self):
    #     result = entry.get()
