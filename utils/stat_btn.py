from tkinter import *
from tkinter import messagebox
from tkmacosx import Button
from other.params import TEXT_CONFIG, BTN_CONFIG


def stat_btn_func(root, user_count, pc_count):
    """
    Функция кнопки "статистика"
    """
    def close_top(toplevel):
        """
        Функция закрытия окна статистики
        """
        toplevel.destroy()

    def save_stat():
        """
        Функция кнопки "сохранить"
        """
        with open("stat.txt", "w") as file:
            file.write(f"Вы выиграли {user_count} раз.\n"
                       f"Компьютер выиграл {pc_count} раз.")
        messagebox.showinfo("Сохранение...", "Статистика успешно сохранена!")

    # global user_count, pc_count

    top = Toplevel(root)
    top.title("Статистика")
    top.geometry("+600+300")
    top.resizable(False, False)
    top.configure(bg="#0e1620")

    # установка top как дочернего окна root
    top.transient(root)

    label = Label(top, text=f"Вы выиграли {user_count} раз.\n"
                            f"Компьютер выиграл {pc_count} раз.", **TEXT_CONFIG)
    label.pack(padx=8, pady=8)

    ok_btn = Button(top, text="OК", **BTN_CONFIG, command=lambda: close_top(top))
    ok_btn.pack(side=LEFT, padx=8, pady=8)

    save_btn = Button(top, text="Сохранить", **BTN_CONFIG, command=save_stat)
    save_btn.pack(side=RIGHT, padx=8, pady=8)

    # установка фокуса на top
    top.grab_set()

    # ожидание закрытия top
    root.wait_window(top)

    # после закрытия top освобождение фокус
    root.grab_release()
