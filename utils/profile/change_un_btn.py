from tkinter import *
from tkinter import messagebox
from tkmacosx import Button
from other.params import BTN_CONFIG
import json


def change_un_btn_func(root):
    """
    Функция для изменения логина
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
        # проверка, что поле не пустое
        if not entry.get():
            messagebox.showwarning("Ошибка",
                                   "Заполните поле!")
            return

        # проверка длины логина
        if len(entry.get()) <= 3:
            messagebox.showwarning("Ошибка",
                                   "Логин должен быть длиннее трёх символов!")
            return

        old_username = const["current_username"]
        new_username = entry.get()

        # проверка, что новый логин не существует в базе данных
        if new_username in reg_data:
            messagebox.showwarning("Ошибка", "Этот логин уже занят!")
            return

        reg_data[new_username] = reg_data.pop(old_username)
        reg_data[new_username]["username"] = new_username

        const["current_username"] = new_username

        messagebox.showinfo("Успех", f"Логин изменён!")

        top.destroy()

    top = Toplevel(root)
    top.title("Изменение логина")
    top.geometry("+590+300")
    top.resizable(False, False)
    top.configure(bg="#0e1620")

    # установка top как дочернего окна root
    top.transient(root)

    # поле ввода логина
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

    # обновление json-файлов
    with open("db.json", 'w') as json_file:
        json.dump(reg_data, json_file, indent=4)
    with open("other/constants.json", 'w') as json_file1:
        json.dump(const, json_file1, indent=4)
