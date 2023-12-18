import json
from utils.authorization import authorization_func
from tkinter import *
from tkmacosx import Button, CircleButton
from utils.stat_btn import stat_btn_func
from utils.widget_operations import clear_widgets_func
from other.params import CIRCLE_BTN_CONFIG, TITLE_CONFIG, BTN_CONFIG
from utils.back_btn import back_btn_func


def profile_btn_func(root, profile_btn, game_title, start_btn,
                     help_btn, gh_btn, main_img_lbl, back_btn_image):
    """
    Функция кнопки "профиль"
    """
    with open("other/constants.json", 'r') as json_file1:
        const = json.load(json_file1)

    def logout_btn_func():
        const["authorization"] = False
        const["current_username"] = ""
        with open("other/constants.json", 'w') as json_file1:
            json.dump(const, json_file1, indent=4)

        clear_widgets_func([back_btn, hello_lbl, stat_btn, logout_btn])

        authorization_func(root, profile_btn, game_title, start_btn,
                           help_btn, gh_btn, main_img_lbl, back_btn_image)

    clear_widgets_func([profile_btn, game_title, start_btn,
                        help_btn, gh_btn, main_img_lbl])

    if const.get("authorization") is False:
        authorization_func(root, profile_btn, game_title, start_btn,
                           help_btn, gh_btn, main_img_lbl, back_btn_image)
    else:
        # кнопка "назад"
        from utils.main_menu import main_menu_func
        back_btn = CircleButton(image=back_btn_image, **CIRCLE_BTN_CONFIG,
                                command=lambda: (back_btn_func(
                                    [back_btn, hello_lbl, stat_btn, logout_btn]), main_menu_func(root)))
        back_btn.place(x="8", y="8")

        hello_lbl = Label(text=f"Привет, {const['current_username']}!", **TITLE_CONFIG)
        hello_lbl.place(x="270", y="16")

        # кнопка "статистика"
        stat_btn = Button(text="Статистика", **BTN_CONFIG,
                          command=lambda: stat_btn_func(root))
        stat_btn.place(x="348", y="192")

        logout_btn = Button(text="Выйти", **BTN_CONFIG, command=lambda: logout_btn_func())
        logout_btn.place(x="350", y="550")
