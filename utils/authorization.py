from tkinter import *
from tkinter import messagebox
from tkmacosx import Button, CircleButton, Radiobutton
import re
import json
from other.params import BACK_BTN_CONFIG, TITLE_CONFIG, TEXT_CONFIG, REG_BTN, BTN_CONFIG, RB_CONFIG
from utils.back_btn import back_btn_func
from utils.widget_operations import clear_widgets_func, clear_entries_func, clear_rb_func


def authorization_func(profile_btn, game_title, start_btn, help_btn, stat_btn, main_img_lbl, back_btn_image):
    """
    Функция для авторизации
    """
    clear_widgets_func([profile_btn, game_title, start_btn, help_btn, stat_btn, main_img_lbl])

    # кнопка "назад" для входа
    back_btn = CircleButton(image=back_btn_image, **BACK_BTN_CONFIG, command=lambda: back_btn_func(
        [back_btn, log_lbl, reg_lbl, email_lbl, email_ent,
         nick_lbl, nick_ent, pass_lbl, pass_ent, reg_btn, next_log_btn],
        {
            profile_btn: (760, 8),
            game_title: (270, 16),
            start_btn: (360, 128),
            help_btn: (357, 160),
            stat_btn: (348, 192),
            main_img_lbl: (460, 365)
        }
    )
                            )
    back_btn.place(x="8", y="8")

    # кнопка "назад" для регистрации
    back_btn1 = CircleButton(image=back_btn_image, **BACK_BTN_CONFIG, command=lambda: (back_btn_func(
        [back_btn1, reg_lbl, male_rb, female_rb, next_reg_btn],
        {
            log_lbl: (270, 16),
            email_lbl: (270, 100),
            email_ent: (270, 140),
            nick_lbl: (270, 200),
            nick_ent: (270, 240),
            pass_lbl: (270, 300),
            pass_ent: (270, 340),
            reg_btn: (270, 370),
            next_log_btn: (360, 558)
        }
    ), clear_entries_func([email_ent, nick_ent, pass_ent]), clear_rb_func([gender_var]))
                             )

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
    # радиокнопка мужского пола
    male_rb = Radiobutton(text="Муж", variable=gender_var, value='M', **RB_CONFIG)
    # радиокнопка женского пола
    female_rb = Radiobutton(text="Жен", variable=gender_var, value='F', **RB_CONFIG)
    # кнопка "регистрация"
    reg_btn = Button(text="Регистрация", **REG_BTN, command=lambda: reg_func())
    # кнопки "далее"
    next_log_btn = Button(text="Далее", **BTN_CONFIG, command=lambda: next_log_btn_func())
    next_reg_btn = Button(text="Далее", **BTN_CONFIG, command=lambda: next_reg_btn_func())

    def next_log_btn_func():
        """
        Функция кнопки "далее" для входа
        """
        print()

    def next_reg_btn_func():
        """
        Функция кнопки "далее" для регистрации
        """
        # проверка, что введённые данные не пусты
        if not email_ent.get() or not nick_ent.get() or not pass_ent.get() or gender_var.get() not in ('M', 'F'):
            messagebox.showwarning("Ошибка", "Заполните все поля регистрации!")
            return

        # проверка длины логина и пароля
        if len(nick_ent.get()) <= 3 or len(pass_ent.get()) <= 3:
            messagebox.showwarning("Ошибка", "Логин и пароль должны быть длиннее трёх символов!")
            return

        # проверка наличия почты паттерну
        email_pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"
        if not re.match(email_pattern, email_ent.get()):
            messagebox.showwarning("Ошибка", "Некорректный адрес электронной почты!")
            return

        # загрузка существующих аккаунтов из файла
        with open("db.json", 'r') as file:
            try:
                accounts = json.load(file)
            except json.decoder.JSONDecodeError:
                accounts = {}

        # проверка на уникальность имени пользователя
        if nick_ent.get() in accounts:
            messagebox.showwarning("Ошибка", "Это имя пользователя уже занято!")
            return

        # добавление нового аккаунта
        registration_data = {
            "email": email_ent.get(),
            "username": nick_ent.get(),
            "password": pass_ent.get(),
            "gender": gender_var.get()
        }
        accounts[nick_ent.get()] = registration_data

        # сохранение обновленных данных в файл
        with open("db.json", 'w') as file:
            json.dump(accounts, file, indent=4)

        messagebox.showinfo("Успех", "Регистрация успешно завершена!")

        data["authorization"] = True
        with open("other/constants.json", 'w') as json_file:
            json.dump(data, json_file, indent=4)

        clear_widgets_func([back_btn1, back_btn, reg_lbl, email_lbl, email_ent, nick_lbl, nick_ent,
                            pass_lbl, pass_ent, next_reg_btn, male_rb, female_rb])

        from utils.main_menu import main_menu_func
        main_menu_func(stat_btn)

    def login_func():
        """
        Функция для входа
        """
        email_ent.delete(0, END)
        nick_ent.delete(0, END)
        pass_ent.delete(0, END)

        log_lbl.place(x="270", y="16")
        email_lbl.place(x="270", y="100")
        email_ent.place(x="270", y="140")
        nick_lbl.place(x="270", y="200")
        nick_ent.place(x="270", y="240")
        pass_lbl.place(x="270", y="300")
        pass_ent.place(x="270", y="340")
        reg_btn.place(x="270", y="370")
        next_log_btn.place(x="360", y="558")

    login_func()

    def reg_func():
        """
        Функция для регистрации
        """
        back_btn1.place(x="8", y="8")

        clear_widgets_func([log_lbl, reg_btn, next_log_btn])

        reg_lbl.place(x="270", y="16")
        next_reg_btn.place(x="360", y="558")
        male_rb.place(x="270", y="420")
        female_rb.place(x="370", y="420")

    with open("other/constants.json", 'r') as json_file:
        data = json.load(json_file)
