from tkinter import messagebox


def close_func(root):
    """
    Функция для закрытия окна игры
    """
    response = messagebox.askyesno("Выход",
                                   "Вы уверены, что хотите выйти?")
    if response:
        root.destroy()
