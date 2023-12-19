from tkinter import *
from tkinter import messagebox
from tkmacosx import Button, CircleButton, Radiobutton
from other.params import (CIRCLE_BTN_CONFIG, TITLE_CONFIG, TEXT_CONFIG,
                          REG_BTN, BTN_CONFIG, RB_CONFIG)
from utils.back_btn import back_btn_func
from utils.widget_operations import clear_widgets_func, clear_entries_func, clear_rb_func
import re
import json


def authorization_func(root, profile_btn, game_title, start_btn, help_btn, leaderboard_btn,
                       gh_btn, main_img_btn, back_btn_image, w_back_btn_image):
    """
    Функция для авторизации
    """
    # открытие json-файла
    with open("other/constants.json", 'r') as json_file1:
        const = json.load(json_file1)

    clear_widgets_func([profile_btn, game_title, start_btn, help_btn,
                        leaderboard_btn, gh_btn, main_img_btn])

    # кнопка "назад" для входа
    from utils.main_menu import main_menu_func
    back_btn = CircleButton(image=back_btn_image, **CIRCLE_BTN_CONFIG,
                            activeimage=w_back_btn_image,
                            command=lambda: (back_btn_func(
                                [back_btn, log_lbl, reg_lbl, email_lbl, email_ent, nick_lbl, nick_ent,
                                 pass_lbl, pass_ent, reg_btn, next_log_btn]), main_menu_func(root)))
    back_btn.place(x="8", y="8")

    # кнопка "назад" для регистрации
    back_btn1 = CircleButton(image=back_btn_image, **CIRCLE_BTN_CONFIG,
                             activeimage=w_back_btn_image,
                             command=lambda: (back_btn_func(
                                 [back_btn1, reg_lbl, gender_lbl, male_rb, female_rb, next_reg_btn]),
                                              clear_entries_func([email_ent, nick_ent, pass_ent]),
                                              clear_rb_func([gender_var]), login_func()))

    # переменная для хранения пола
    gender_var = StringVar()
    gender_var.set(NONE)

    # заголовок "вход"
    log_lbl = Label(text="Вход", **TITLE_CONFIG)
    # заголовок "регистрация"
    reg_lbl = Label(text="Регистрация", **TITLE_CONFIG)
    # подпись "почта"
    email_lbl = Label(text="Почта", **TEXT_CONFIG)
    # ввод почты
    email_ent = Entry()
    # подпись "логин"
    nick_lbl = Label(text="Логин", **TEXT_CONFIG)
    # ввод логина
    nick_ent = Entry()
    # подпись "пароль"
    pass_lbl = Label(text="Пароль", **TEXT_CONFIG)
    # ввод пароля
    pass_ent = Entry(show='*')
    # подпись "ваш пол"
    gender_lbl = Label(text="Ваш пол", **TEXT_CONFIG)
    # радиокнопка мужского пола
    male_rb = Radiobutton(text="Муж", variable=gender_var,
                          value='M', **RB_CONFIG)
    # радиокнопка женского пола
    female_rb = Radiobutton(text="Жен", variable=gender_var,
                            value='F', **RB_CONFIG)
    # кнопка "регистрация"
    reg_btn = Button(text="Регистрация", **REG_BTN,
                     command=lambda: reg_func())
    # кнопки "далее"
    next_log_btn = Button(text="Далее", **BTN_CONFIG,
                          command=lambda: next_log_btn_func())
    next_reg_btn = Button(text="Далее", **BTN_CONFIG,
                          command=lambda: next_reg_btn_func())

    def next_log_btn_func():
        """
        Функция кнопки "далее" для входа
        """
        # проверка, что введённые данные не пусты
        if not email_ent.get() or not nick_ent.get() or not pass_ent.get():
            messagebox.showwarning("Ошибка",
                                   "Заполните все поля входа!")
            return

        # загрузка существующих аккаунтов из файла
        with open("db.json", 'r') as file:
            try:
                accounts = json.load(file)
            except json.decoder.JSONDecodeError:
                accounts = {}

        # проверка наличия аккаунта с введенным логином
        username = nick_ent.get()
        if username not in accounts:
            messagebox.showwarning("Ошибка",
                                   "Неверный логин или пароль!")
            return

        # проверка корректности введенного пароля
        if accounts[username]["password"] != pass_ent.get():
            messagebox.showwarning("Ошибка",
                                   "Неверный логин или пароль!")
            return

        messagebox.showinfo("Успех",
                            f"Добро пожаловать, {username}!")

        const["authorization"] = True
        const["current_username"] = username
        with open("other/constants.json", 'w') as json_file1:
            json.dump(const, json_file1, indent=4)

        clear_widgets_func([back_btn, back_btn1, reg_lbl, email_lbl, email_ent, nick_lbl, nick_ent,
                            pass_lbl, pass_ent, next_log_btn, gender_lbl, male_rb, female_rb, reg_btn])

        main_menu_func(root)

    def next_reg_btn_func():
        """
        Функция кнопки "далее" для регистрации
        """
        # проверка, что введённые данные не пусты
        if (not email_ent.get() or not nick_ent.get() or not pass_ent.get()
                or gender_var.get() not in ('M', 'F')):
            messagebox.showwarning("Ошибка",
                                   "Заполните все поля регистрации!")
            return

        # проверка длины логина и пароля
        if len(nick_ent.get()) <= 3 or len(pass_ent.get()) <= 3:
            messagebox.showwarning("Ошибка",
                                   "Логин и пароль должны быть длиннее трёх символов!")
            return

        # проверка наличия почты паттерну
        email_pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"
        if not re.match(email_pattern, email_ent.get()):
            messagebox.showwarning("Ошибка",
                                   "Некорректный адрес электронной почты!")
            return

        # загрузка существующих аккаунтов из файла
        with open("db.json", 'r') as file:
            try:
                accounts = json.load(file)
            except json.decoder.JSONDecodeError:
                accounts = {}

        # проверка на уникальность имени пользователя
        username = nick_ent.get()
        if username in accounts:
            messagebox.showwarning("Ошибка",
                                   "Это имя пользователя уже занято!")
            return

        # добавление нового аккаунта
        reg_data = {
            "email": email_ent.get(),
            "username": nick_ent.get(),
            "password": pass_ent.get(),
            "gender": gender_var.get(),
            "user_wins": 0,
            "pc_wins": 0
        }
        accounts[nick_ent.get()] = reg_data

        with open("db.json", 'w') as file:
            json.dump(accounts, file, indent=4)

        const["authorization"] = True
        const["current_username"] = username
        with open("other/constants.json", 'w') as json_file1:
            json.dump(const, json_file1, indent=4)

        messagebox.showinfo("Успех",
                            f"Добро пожаловать, {username}!")

        clear_widgets_func([back_btn, back_btn1, reg_lbl, email_lbl, email_ent, nick_lbl, nick_ent,
                            pass_lbl, pass_ent, next_log_btn, next_reg_btn, gender_lbl, male_rb, female_rb])

        main_menu_func(root)

    def login_func():
        """
        Функция для входа
        """
        log_lbl.place(x="350", y="16")
        email_lbl.place(x="370", y="110")
        email_ent.place(x="305", y="140")
        nick_lbl.place(x="370", y="210")
        nick_ent.place(x="305", y="240")
        pass_lbl.place(x="370", y="310")
        pass_ent.place(x="305", y="340")
        reg_btn.place(x="400", y="370")
        next_log_btn.place(x="360", y="558")

    login_func()

    def reg_func():
        """
        Функция для регистрации
        """
        back_btn1.place(x="8", y="8")

        clear_widgets_func([log_lbl, reg_btn, next_log_btn])

        reg_lbl.place(x="285", y="16")
        next_reg_btn.place(x="360", y="558")
        gender_lbl.place(x="370", y="390")
        male_rb.place(x="310", y="420")
        female_rb.place(x="430", y="420")
