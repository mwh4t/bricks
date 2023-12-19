from tkinter import *
from tkinter import messagebox
from tkmacosx import Button
from other.params import TEXT_CONFIG, BTN_CONFIG
import json


def stat_btn_func(root):
    """
    Функция кнопки "статистика"
    """
    # открытие json-файлов
    with open("other/constants.json", 'r') as json_file1:
        const = json.load(json_file1)
    with open("db.json", 'r') as json_file:
        reg_data = json.load(json_file)

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
            if const.get("current_username") in reg_data:
                file.write(f"Вы выиграли {reg_data[const['current_username']]['user_wins']} раз.\n"
                           f"Компьютер выиграл {reg_data[const['current_username']]['pc_wins']} раз.")
        messagebox.showinfo("Сохранение...",
                            "Статистика успешно сохранена!")

    top = Toplevel(root)
    top.title("Статистика")
    top.geometry("+590+300")
    top.resizable(False, False)
    top.configure(bg="#0e1620")

    # установка top как дочернего окна root
    top.transient(root)

    if const.get("current_username") in reg_data:
        label = Label(top, text=f"Вы выиграли {reg_data[const['current_username']]['user_wins']} раз.\n"
                                f"Компьютер выиграл {reg_data[const['current_username']]['pc_wins']} раз.",
                      **TEXT_CONFIG)
        label.pack(padx=8, pady=8)

    # кнопка "ОК"
    ok_btn = Button(top, text="OК", **BTN_CONFIG,
                    command=lambda: close_top(top))
    ok_btn.pack(side=LEFT, padx=8, pady=8)

    # кнопка "сохранить"
    save_btn = Button(top, text="Сохранить", **BTN_CONFIG,
                      command=save_stat)
    save_btn.pack(side=RIGHT, padx=8, pady=8)

    # установка фокуса на top
    top.grab_set()
    # ожидание закрытия top
    root.wait_window(top)
    # после закрытия top освобождение фокуса
    root.grab_release()
