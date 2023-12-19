from tkinter import *
from tkinter import messagebox
from tkmacosx import Button
from other.params import BTN_CONFIG
import re
import json


def change_email_btn_func(root):
    """
    Функция для изменения почты
    """
    # открытие json-файлов
    with open("other/constants.json", 'r') as json_file1:
        const = json.load(json_file1)
    with open("db.json", 'r') as json_file:
        reg_data = json.load(json_file)

    def next_btn_func():
        """
        Функция кнопки "далее"
        """
        nonlocal reg_data

        # проверка, что поле не пустое
        if not entry.get():
            messagebox.showwarning("Ошибка",
                                   "Заполните поле!")
            return

        # проверка наличия почты паттерну
        email_pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"
        if not re.match(email_pattern, entry.get()):
            messagebox.showwarning("Ошибка",
                                   "Некорректный адрес электронной почты!")
            return

        username = const["current_username"]
        new_email = entry.get()

        # проверка, что новый пароль не совпадает со старым
        if new_email == reg_data[username]["email"]:
            messagebox.showwarning("Ошибка",
                                   "Новая почта совпадает со старой!")
            return

        reg_data[username]["email"] = new_email

        messagebox.showinfo("Успех",
                            "Почта изменена!")

        top.destroy()

    top = Toplevel(root)
    top.title("Изменение почты")
    top.geometry("+590+300")
    top.resizable(False, False)
    top.configure(bg="#0e1620")

    # установка top как дочернего окна root
    top.transient(root)

    # поле ввода почты
    entry = Entry(top)
    entry.pack(padx=8, pady=8)

    # кнопка "далее"
    next_btn = Button(top, text="Далее", **BTN_CONFIG,
                      command=lambda: next_btn_func())
    next_btn.pack(side=TOP, padx=8, pady=8)

    # установка фокуса на top
    top.grab_set()
    # ожидание закрытия top
    root.wait_window(top)
    # после закрытия top освобождение фокуса
    root.grab_release()

    # обновление db.json
    with open("db.json", 'w') as json_file:
        json.dump(reg_data, json_file, indent=4)
