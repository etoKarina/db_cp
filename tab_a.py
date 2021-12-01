import tkinter as tk
from tkinter import messagebox, RIGHT, LEFT, TOP, IntVar


class Example(tk.Frame):
    def __init__(self, parent, restoraunt):
        super().__init__(parent)

        self.parent = parent
        self.restoraunt = restoraunt
        self.init_ui()
        self.order_ticks = []
        self.current_order_dish_ids = []

    def init_ui(self):
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side=LEFT)

        self.submenu_frame = tk.Frame(self)
        self.submenu_frame.pack(side=TOP)

        self.button_error = tk.Button(self.button_frame, text='Сделать заказ', command=self.make_order_submenu)
        self.button_error.pack()

        self.button_error = tk.Button(self.button_frame, text='Актуальное меню', command=self.actual_menu)
        self.button_error.pack()

        self.pack()

    def summon_error(self):  # TODO: сделать декоратором для функций, кидающих ошибки
        try:
            self.restoraunt._throw_error()
        except Exception as e:
            messagebox.showerror('ERROR', e)

    def clear_submenu(self):
        for widget in self.submenu_frame.winfo_children():
            widget.destroy()

    def refresh_menu(self):
        self.order_ticks = []
        self.current_order_dish_ids = []
        dishes = self.restoraunt.get_actual_menu()
        height = len(dishes)
        if height:
            for i in range(height):  # Rows
                tk.Label(self.submenu_frame, text=dishes[i][1]).grid(row=i + 1, column=0)
                tk.Label(self.submenu_frame, text=dishes[i][2]).grid(row=i + 1, column=1)
                self.order_ticks.append(IntVar())
                self.current_order_dish_ids.append(dishes[i][0])
                tk.Checkbutton(self.submenu_frame, variable=self.order_ticks[-1]).grid(row=i + 1, column=2)
            tk.Button(self.submenu_frame, text='Заказать!', command=self.make_order).grid(row=height + 1, column=1)
        else:
            tk.Label(self.submenu_frame, text='нечего заказать!').grid(row=height + 1, column=1)

    def make_order_submenu(self):
        self.clear_submenu()

        tk.Label(self.submenu_frame, text='Блюдо').grid(row=0, column=0)
        tk.Label(self.submenu_frame, text='Цена').grid(row=0, column=1)
        self.refresh_menu()

    def make_order(self):

        chosen_dishes = [dish_id for dish_id, is_chosen in zip(self.current_order_dish_ids, self.order_ticks) if
                         is_chosen.get()]

        self.restoraunt.order(chosen_dishes)
        if chosen_dishes:
            messagebox.showinfo('заказ сделан!', 'заказ сделан!')
        self.refresh_menu()

    def actual_menu(self):
        self.clear_submenu()
        dishes = self.restoraunt.get_actual_menu()
        if dishes:
            height = len(dishes)
            width = len(dishes[0])

            for i in range(height):  # Rows
                for j in range(width):  # Columns
                    b = tk.Label(self.submenu_frame, text=dishes[i][j])
                    b.grid(row=i, column=j)
        else:
            tk.Label(self.submenu_frame, text='нечего заказать!').pack()

    def on_select(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        self.var.set(value)
