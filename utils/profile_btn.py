import json
from utils.authorization import authorization_func
from tkinter import *
from tkmacosx import CircleButton
from utils.widget_operations import clear_widgets_func
from other.params import BACK_BTN_CONFIG, TITLE_CONFIG
from utils.back_btn import back_btn_func

with open("other/constants.json", 'r') as json_file:
    loaded_constants = json.load(json_file)


def profile_btn_func(root, profile_btn, game_title, start_btn, help_btn,
                     stat_btn, main_img_lbl, back_btn_image):
    """
    Функция кнопки "профиль"
    """
    clear_widgets_func([profile_btn, game_title, start_btn,
                        help_btn, stat_btn, main_img_lbl])

    if loaded_constants.get("authorization") is False:
        authorization_func(root, profile_btn, game_title, start_btn, help_btn,
                           stat_btn, main_img_lbl, back_btn_image)
    else:
        # кнопка "назад"
        from utils.main_menu import main_menu_func
        back_btn = CircleButton(image=back_btn_image, **BACK_BTN_CONFIG,
                                command=lambda: (back_btn_func(
                                    [back_btn, hello_lbl]), main_menu_func(root)))
        back_btn.place(x="8", y="8")

        hello_lbl = Label(text="Привет, <Аккаунт>!", **TITLE_CONFIG)
        hello_lbl.place(x="270", y="16")
