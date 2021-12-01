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

        self.frame = tk.Frame(self)
        self.frame.pack(side=RIGHT)

        self.button2 = tk.Button(self.button_frame, text='Список ингредиентов')
        self.button2.pack(side=TOP)

        self.button3 = tk.Button(self.button_frame, text='абоба')
        self.button3.pack(side=TOP)

        # entry1 = tk.Entry(self)
        # label1 = tk.Label(self, text='kago')

    # def on_click(self):
    #     result = entry.get()
