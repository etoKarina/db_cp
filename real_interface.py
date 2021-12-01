from tkinter import Tk, ttk
import tkinter as tk
from business_logic import Restoraunt

from tab_a import Example as TabA
from tab_b import Example as TabB
from tab_c import Example as TabC
from tab_d import Example as TabD


class MainWindow(tk.Frame):
    def __init__(self, parent, restoraunt):
        super().__init__(parent)

        self.parent = parent
        self.restoraunt = restoraunt

        self.parent.title('Gourmets')

        self.init_ui()

    def init_ui(self):
        self.parent['padx'] = 10
        self.parent['pady'] = 10

        self.notebook = ttk.Notebook(self, width=1000, height=700)

        a_tab = TabA(self.notebook, self.restoraunt)
        b_tab = TabB(self.notebook, self.restoraunt)
        c_tab = TabC(self.notebook, self.restoraunt)
        d_tab = TabD(self.notebook, self.restoraunt)

        self.notebook.add(a_tab, text="Посетителям")
        self.notebook.add(b_tab, text="Поставщикам")
        self.notebook.add(c_tab, text="Персоналу")
        self.notebook.add(d_tab, text="Документация")

        self.notebook.pack()

        self.pack()


if __name__ == '__main__':
    root = Tk()
    root.title('Gourmets')
    restoraunt = Restoraunt()
    ex = MainWindow(root, restoraunt)
    root.geometry("800x600")
    root.mainloop()
