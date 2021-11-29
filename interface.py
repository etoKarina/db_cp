import tkinter as tk
from business_logic import Restoraunt


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        # init db
        self.restoraunt = Restoraunt()

        self.somebutton = tk.Button(text='push me')
        self.somebutton.pack()

        self.somebutton.bind('<Button-1>', self.print_contents)

        self.somelabel = tk.Label(text='here comes something')
        self.somelabel.pack()

    def print_contents(self, event):
        result = self.restoraunt.db.get_all_products()
        self.somelabel['text'] = result


root = tk.Tk()
myapp = App(root)
myapp.mainloop()
