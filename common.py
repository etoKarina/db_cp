from tkinter import messagebox

def propagate_error_to_ui(fun):
    def wrapped(*args, **kwargs):

        try:
            res = fun(*args, **kwargs)
            return res
        except Exception as e:
            messagebox.showerror('ERROR', e)
            raise e

    return wrapped