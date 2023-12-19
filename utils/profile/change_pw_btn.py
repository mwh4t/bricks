from tkinter import *
from tkinter import messagebox
from tkmacosx import Button
from other.params import BTN_CONFIG
import json


def change_pw_btn_func(root):
    """
    Функция для изменения пароля
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

        # проверка длины пароля
        if len(entry.get()) <= 3:
            messagebox.showwarning("Ошибка",
                                   "Пароль должен быть длиннее трёх символов!")
            return

        username = const["current_username"]
        new_password = entry.get()

        # проверка, что новый пароль не совпадает со старым
        if new_password == reg_data[username]["password"]:
            messagebox.showwarning("Ошибка",
                                   "Новый пароль совпадает со старым!")
            return

        reg_data[username]["password"] = new_password

        messagebox.showinfo("Успех",
                            "Пароль изменён!")

        top.destroy()

    top = Toplevel(root)
    top.title("Изменение пароля")
    top.geometry("+590+300")
    top.resizable(False, False)
    top.configure(bg="#0e1620")

    # установка top как дочернего окна root
    top.transient(root)

    # поле ввода пароля
    entry = Entry(top, show='*')
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
