from tkinter import *
from tkmacosx import Button, CircleButton
from utils.authorization import authorization_func
from utils.stat_btn import stat_btn_func
from utils.profile.change_email_btn import change_email_btn_func
from utils.profile.change_un_btn import change_un_btn_func
from utils.profile.change_pw_btn import change_pw_btn_func
from utils.widget_operations import clear_widgets_func
from other.params import CIRCLE_BTN_CONFIG, TITLE_CONFIG, BTN_CONFIG, TEXT_CONFIG
from utils.back_btn import back_btn_func
import json


def profile_btn_func(root, settings_image, w_settings_image, profile_btn, game_title, start_btn, help_btn,
                     leaderboard_btn, gh_btn, main_img_btn, back_btn_image, w_back_btn_image):
    """
    Функция кнопки "профиль"
    """
    # открытие json-файла
    with open("other/constants.json", 'r') as json_file1:
        const = json.load(json_file1)

    def logout_btn_func():
        """
        Функция выхода из аккаунта
        """
        const["authorization"] = False
        const["current_username"] = ""
        with open("other/constants.json", 'w') as json_file1:
            json.dump(const, json_file1, indent=4)

        clear_widgets_func([back_btn, profile_lbl, email_lbl, change_email_btn, username_lbl,
                            change_un_btn, password_lbl, change_pw_btn, stat_btn, logout_btn])

        authorization_func(root, profile_btn, game_title, start_btn, help_btn, leaderboard_btn,
                           gh_btn, main_img_btn, back_btn_image, w_back_btn_image)

    clear_widgets_func([profile_btn, game_title, start_btn, help_btn,
                        leaderboard_btn, gh_btn, main_img_btn])

    if const.get("authorization") is False:
        authorization_func(root, profile_btn, game_title, start_btn, help_btn, leaderboard_btn,
                           gh_btn, main_img_btn, back_btn_image, w_back_btn_image)
    else:
        # кнопка "назад"
        from utils.main_menu import main_menu_func
        back_btn = CircleButton(image=back_btn_image, **CIRCLE_BTN_CONFIG, activeimage=w_back_btn_image,
                                command=lambda: (back_btn_func(
                                    [back_btn, profile_lbl, email_lbl, change_email_btn, username_lbl, change_un_btn,
                                     password_lbl, change_pw_btn, stat_btn, logout_btn]), main_menu_func(root)))
        back_btn.place(x="8", y="8")

        # открытие json-файла
        with open("db.json", 'r') as json_file:
            reg_data = json.load(json_file)

        # заголовок "профиль"
        profile_lbl = Label(text="Профиль", **TITLE_CONFIG)
        profile_lbl.place(x="320", y="16")

        # кнопка "статистика"
        stat_btn = Button(text="Статистика", **BTN_CONFIG,
                          command=lambda: stat_btn_func(root))
        stat_btn.place(x="340", y="250")

        # подпись "почта"
        email_lbl = Label(text=f"Почта: {reg_data[const['current_username']]['email']}",
                          **TEXT_CONFIG)
        email_lbl.place(x="330", y="100")

        # кнопка "изменить почту"
        change_email_btn = CircleButton(image=settings_image, **CIRCLE_BTN_CONFIG,
                                        activeimage=w_settings_image,
                                        command=lambda: change_email_btn_func(root))
        change_email_btn.config(width=28)
        change_email_btn.place(x="305", y="98")

        # подпись "логин"
        username_lbl = Label(text=f"Логин: {const['current_username']}",
                             **TEXT_CONFIG)
        username_lbl.place(x="330", y="150")

        # кнопка "изменить логин"
        change_un_btn = CircleButton(image=settings_image, activeimage=w_settings_image,
                                     **CIRCLE_BTN_CONFIG, command=lambda: change_un_btn_func(root))
        change_un_btn.config(width=28)
        change_un_btn.place(x="305", y="148")

        # подпись "пароль"
        password_var = StringVar(value='*' * len(reg_data[const['current_username']]['password']))
        password_lbl = Label(text="Пароль: {}".format(password_var.get()), **TEXT_CONFIG)
        password_lbl.place(x="330", y="200")

        # кнопка "изменить пароль"
        change_pw_btn = CircleButton(image=settings_image, activeimage=w_settings_image,
                                     **CIRCLE_BTN_CONFIG, command=lambda: change_pw_btn_func(root))
        change_pw_btn.config(width=28)
        change_pw_btn.place(x="305", y="198")

        # кнопка "выйти"
        logout_btn = Button(text="Выйти", **BTN_CONFIG,
                            command=lambda: logout_btn_func())
        logout_btn.place(x="350", y="550")
