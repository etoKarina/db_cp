import tkinter as tk
from tkinter import messagebox, RIGHT, LEFT, TOP


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

        self.button_error = tk.Button(self.button_frame, text='Сделать заказ', command=self.make_order)
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

    def make_order(self):  # TODO: сделать декоратором для функций, кидающих ошибки
        self.clear_submenu()
        self.submenu_frame.lb = tk.Label(self.submenu_frame, text='makeorder')
        self.submenu_frame.lb.pack()

    def actual_menu(self):  # TODO: сделать декоратором для функций, кидающих ошибки
        self.clear_submenu()
        self.submenu_frame.lb = tk.Label(self.submenu_frame, text='actualmenu')
        self.submenu_frame.lb.pack(side=TOP)

    def on_select(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        self.var.set(value)
