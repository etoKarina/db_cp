import tkinter as tk
from tkinter import messagebox


class Example(tk.Frame):
    def __init__(self, parent, restoraunt):
        super().__init__(parent)

        self.parent = parent
        self.restoraunt = restoraunt
        self.init_ui()

    def init_ui(self):
        self.pack(fill=tk.BOTH, expand=1)

        acts = ['Scarlett Johansson', 'Rachel Weiss', 'Natalie Portman', 'Jessica Alba']

        self.lb = tk.Listbox(self)
        for i in acts:
            self.lb.insert(tk.END, i)
            self.lb.bind("<<ListboxSelect>>", self.on_select)
            self.lb.pack(pady=15)

        self.var = tk.StringVar()
        self.label = tk.Label(self, text=0, textvariable=self.var)
        self.label.pack()

        self.button_error = tk.Button(self, text='iamerror', command=self.summon_error)
        self.button_error.pack()

        self.pack()

    def summon_error(self):  # TODO: сделать декоратором для функций, кидающих ошибки
        try:
            self.restoraunt._throw_error()
        except Exception as e:
            messagebox.showerror('ERROR', e)

    def on_select(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        self.var.set(value)
