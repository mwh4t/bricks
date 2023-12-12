from tkinter import *
from tkmacosx import Button, CircleButton
from other.params import BACK_BTN_CONFIG, TITLE_CONFIG, TEXT_CONFIG, LOGIN_BTN, BTN_CONFIG
from utils.back_btn import back_btn_func


def authorization_func(profile_btn, game_title, start_btn, help_btn, stat_btn, main_img_lbl):
    """
    Функция для авторизации
    """
    # кнопка "назад"
    back_btn_image = PhotoImage(file="other/images/back.png")
    back_btn = CircleButton(image=back_btn_image, **BACK_BTN_CONFIG, command=lambda: back_btn_func(
        [back_btn, reg_lbl, reg_mail_lbl, reg_mail_ent,
         reg_nick_lbl, reg_nick_ent, reg_pass_lbl, reg_pass_ent,
         next_btn, log_btn, log_lbl],
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

    # заголовок "регистрация"
    reg_lbl = Label(text="Регистрация", **TITLE_CONFIG)

    # подпись "почта"
    reg_mail_lbl = Label(text="Почта", **TEXT_CONFIG)

    # ввод почты
    reg_mail_ent = Entry()

    # подпись "логин"
    reg_nick_lbl = Label(text="Логин", **TEXT_CONFIG)

    # ввод логина
    reg_nick_ent = Entry()

    # подпись "пароль"
    reg_pass_lbl = Label(text="Пароль", **TEXT_CONFIG)

    # ввод пароля
    reg_pass_ent = Entry()

    # кнопка "вход"
    log_btn = Button(text="Вход", **LOGIN_BTN, command=lambda: login_func())

    # кнопка "далее"
    next_btn = Button(text="Далее", **BTN_CONFIG)

    # заголовок "Вход"
    log_lbl = Label(text="Вход", **TITLE_CONFIG)

    def reg_func():
        """
        Функция для регистрации
        """
        reg_lbl.place(x="270", y="16")
        reg_mail_lbl.place(x="270", y="100")
        reg_mail_ent.place(x="270", y="140")
        reg_nick_lbl.place(x="270", y="200")
        reg_nick_ent.place(x="270", y="240")
        reg_pass_lbl.place(x="270", y="300")
        reg_pass_ent.place(x="270", y="340")
        log_btn.place(x="270", y="370")
        next_btn.place(x="360", y="558")

    reg_func()

    def login_func():
        """
        Функция для входа
        """
        reg_lbl.place_forget()
        reg_mail_lbl.place_forget()
        reg_mail_ent.place_forget()
        reg_nick_lbl.place_forget()
        reg_nick_ent.place_forget()
        reg_pass_lbl.place_forget()
        reg_pass_ent.place_forget()
        next_btn.place_forget()
        log_btn.place_forget()

        log_lbl.place(x="270", y="16")
