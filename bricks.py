from tkinter import *
from tkmacosx import Button
from utils.main_menu import main_menu_func
from utils.close import close_func
from utils.stat_btn import stat_btn_func
from other.params import BTN_CONFIG


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

# кнопка "статистика"
stat_btn = Button(text="Статистика", **BTN_CONFIG, command=lambda: stat_btn_func(root))
stat_btn.place(x="348", y="192")

main_menu_func(stat_btn)

# запуск основного цикла
root.mainloop()
