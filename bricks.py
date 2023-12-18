from tkinter import *
from utils.close import close_func
from utils.main_menu import main_menu_func


# создание основного окна
root = Tk()
root.title("Кирпичи")
root.geometry("800x600")
root.geometry("+300+100")
root.resizable(False, False)

# цвет фона
root.configure(bg="#0e1620")

# обработчик закрытия окна
root.protocol("WM_DELETE_WINDOW", lambda: close_func(root))

main_menu_func(root)

# запуск основного цикла
root.mainloop()
