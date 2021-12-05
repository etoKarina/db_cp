from tkinter import Tk, ttk
import tkinter as tk
from business_logic import Restoraunt

from form_for_clients import Example as TabA
from form_for_suppliers import Example as TabB
from form_for_workers import Example as TabC
from form_for_documents import Example as TabD


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

        tab_for_clients = TabA(self.notebook, self.restoraunt)
        tab_for_suppliers = TabB(self.notebook, self.restoraunt)
        tab_for_workers = TabC(self.notebook, self.restoraunt)
        tab_for_documents = TabD(self.notebook, self.restoraunt)

        self.notebook.add(tab_for_clients, text="Посетителям")
        self.notebook.add(tab_for_suppliers, text="Поставщикам")
        self.notebook.add(tab_for_workers, text="Персоналу")
        self.notebook.add(tab_for_documents, text="Документация")

        self.notebook.pack()

        self.pack()


if __name__ == '__main__':
    root = Tk()
    root.title('Gourmets')
    restoraunt = Restoraunt()
    ex = MainWindow(root, restoraunt)
    root.geometry("800x600")
    root.mainloop()
