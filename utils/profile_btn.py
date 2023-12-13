from utils.authorization import authorization_func
from tkinter import *
from tkmacosx import CircleButton
from other.params import BACK_BTN_CONFIG, TITLE_CONFIG
from utils.back_btn import back_btn_func


def profile_btn_func(profile_btn, game_title, start_btn, help_btn, stat_btn, main_img_lbl,
                     authorization, back_btn_image):
    """
    Функция кнопки "профиль"
    """
    profile_btn.place_forget()
    game_title.place_forget()
    start_btn.place_forget()
    help_btn.place_forget()
    stat_btn.place_forget()
    main_img_lbl.place_forget()

    if not authorization:
        authorization_func(profile_btn, game_title, start_btn, help_btn, stat_btn, main_img_lbl, back_btn_image)
    else:
        # кнопка "назад"
        back_btn = CircleButton(image=back_btn_image, **BACK_BTN_CONFIG, command=lambda: back_btn_func(
            [back_btn, hello_lbl],
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

        hello_lbl = Label(text="Привет, <Аккаунт>!", **TITLE_CONFIG)
        hello_lbl.place(x="270", y="16")
