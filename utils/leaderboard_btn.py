from tkinter import *
from tkmacosx import Button
from other.params import TEXT_CONFIG, BTN_CONFIG
import json


def leaderboard_btn_func(root):
    """
    Функция кнопки "таблица лидеров"
    """
    def close_top(toplevel):
        """
        Функция закрытия окна статистики
        """
        toplevel.destroy()

    top = Toplevel(root)
    top.title("Таблица лидеров")
    top.geometry("+620+300")
    top.resizable(False, False)
    top.configure(bg="#0e1620")

    # установка top как дочернего окна root
    top.transient(root)

    # вывод топ-3 аккаунтов
    try:
        with open("db.json", 'r') as json_file:
            reg_data = json.load(json_file)

        # сортировка аккаунтов по убыванию количества побед
        sorted_accounts = sorted(reg_data.items(), key=lambda x: x[1]["user_wins"], reverse=True)

        for i, (username, data) in enumerate(sorted_accounts[:3]):
            label = Label(top, text=f"{i+1}. {username}: {data['user_wins']} побед", **TEXT_CONFIG)
            label.pack(padx=8, pady=8, anchor='w')
    except json.decoder.JSONDecodeError:
        label = Label(top, text="Не найдено аккаунтов!", **TEXT_CONFIG)
        label.pack(padx=8, pady=8, anchor="center")

    # кнопка "ОК"
    ok_btn = Button(top, text="OК", **BTN_CONFIG,
                    command=lambda: close_top(top))
    ok_btn.pack(side=TOP, padx=8, pady=8)

    # установка фокуса на top
    top.grab_set()
    # ожидание закрытия top
    root.wait_window(top)
    # после закрытия top освобождение фокус
    root.grab_release()
