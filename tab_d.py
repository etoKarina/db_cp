import tkinter as tk
from business_logic import Restoraunt


class Example(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()
        self.restoraunt = Restoraunt()

    def init_ui(self):
        # self.button = tk.Button(self, text='Список блюд', command=self.on_click)
        # self.button.pack()
        #
        # self.pack()

        self.button2 = tk.Button(self, text='Список ингредиентов', command=self.on_click3)
        self.button2.pack()
        self.table = tk.Frame(self)
        self.table.pack()

        # self.pack()
        #
        # self.somelabel = tk.Label(self, text='here comes something')
        # self.somelabel.pack()

    def on_click(self):
        result = self.restoraunt.db.get_all_dish()
        self.somelabel['text'] = result

    def on_click2(self):
        result = self.restoraunt.db.get_all_products()
        self.somelabel['text'] = result

    def on_click3(self):
        products = self.restoraunt.db.get_all_products()
        height = len(products)
        width = 5

        for i in range(height):  # Rows
            for j in range(width):  # Columns
                b = tk.Label(self.table, text=products[i][j])
                b.grid(row=i, column=j)
