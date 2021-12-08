import tkinter as tk
from tkinter import Tk, RIGHT, BOTH, RAISED, LEFT, Y, TOP
from common import propagate_error_to_ui


class Example(tk.Frame):
    def __init__(self, parent, restoraunt):
        super().__init__(parent)

        self.parent = parent
        self.restoraunt = restoraunt
        self.init_ui()

    def init_ui(self):
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side=LEFT, padx=10, pady=10)

        self.submenu_frame = tk.Frame(self)
        self.submenu_frame.pack(side=TOP, padx=10, pady=10)

        self.add_new_product = tk.Button(self.button_frame, text='Добавить новый продукт', command=self.add_product_submenu)
        self.add_new_product.pack()

        self.delete_product = tk.Button(self.button_frame, text='Удалить продукт', command=self.delete_product_submenu)
        self.delete_product.pack()

        self.pack()

    def clear_submenu(self):
        for widget in self.submenu_frame.winfo_children():
            widget.destroy()

    def add_product_submenu(self):
        self.clear_submenu()
        self.name = tk.StringVar(self)
        self.price = tk.StringVar(self)
        self.type = tk.StringVar(self)
        self.exp_date = tk.StringVar(self)

        self.label_1 = tk.Label(self.submenu_frame, text="Введите название продукта:")
        self.label_1.grid(row=0, column=0)

        self.entry_for_products_name = tk.Entry(self.submenu_frame, textvariable=self.name)
        self.entry_for_products_name.grid(row=0, column=1)

        self.label_2 = tk.Label(self.submenu_frame, text="Введите тип продукта:")
        self.label_2.grid(row=1, column=0)

        self.entry_for_products_type = tk.Entry(self.submenu_frame, textvariable=self.type)
        self.entry_for_products_type.grid(row=1, column=1)

        self.label_3 = tk.Label(self.submenu_frame, text="Введите цену продукта:")
        self.label_3.grid(row=2, column=0)

        self.entry_for_products_price = tk.Entry(self.submenu_frame, textvariable=self.price)
        self.entry_for_products_price.grid(row=2, column=1)

        self.label_4 = tk.Label(self.submenu_frame, text="Введите срок годности:")
        self.label_4.grid(row=3, column=0)

        self.entry_for_products_date = tk.Entry(self.submenu_frame, textvariable=self.exp_date)
        self.entry_for_products_date.grid(row=3, column=1)

        self.sending_new_product = tk.Button(self.submenu_frame, text='Ок', command=self.send_products)
        self.sending_new_product.grid(row=4, column=0)

        self.clear_button = tk.Button(self.submenu_frame, text='Отмена', command=self.clear_submenu)
        self.clear_button.grid(row=4, column=1)

    def delete_product_submenu(self):
        self.clear_submenu()
        self.delete_id = tk.StringVar(self)

        tk.Label(self.submenu_frame, text="Введите id продукта, которое хотиет удалить:").grid(row=0, column=0)

        self.entry_for_products_name = tk.Entry(self.submenu_frame, textvariable=self.delete_id)
        self.entry_for_products_name.grid(row=0, column=1)

        self.delete_product = tk.Button(self.submenu_frame, text='Ок', command=self.delete_product)
        self.delete_product.grid(row=1, column=1)

    def send_products(self):
        self.clear_submenu()
        propagate_error_to_ui(self.restoraunt.add_product)(self.name.get(), self.type.get(), self.price.get(), self.exp_date.get())

    def delete_product(self):
        self.clear_submenu()
        # TODO: оберунть в propaget_error_to_ui и убрать приведение к инту в бизнес логику как в add_product
        self.restoraunt.delete_product(int(self.delete_id.get()))

