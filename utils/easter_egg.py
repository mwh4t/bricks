from tkinter import *
from tkmacosx import CircleButton
from utils.widget_operations import clear_widgets_func
from other.params import CIRCLE_BTN_CONFIG
from utils.back_btn import back_btn_func


def easter_egg_func(root, game_title, profile_btn, start_btn, help_btn, leaderboard_btn,
                    gh_btn, main_img_btn, egg_image, back_btn_image, w_back_btn_image):
    """
    Функция пасхалки
    """
    clear_widgets_func([game_title, profile_btn, start_btn, help_btn,
                        leaderboard_btn, gh_btn, main_img_btn])

    # кнопка "назад"
    from utils.main_menu import main_menu_func
    back_btn = CircleButton(image=back_btn_image, **CIRCLE_BTN_CONFIG,
                            activeimage=w_back_btn_image,
                            command=lambda: (back_btn_func(
                                [back_btn, egg_lbl]), main_menu_func(root)))
    back_btn.place(x="8", y="8")

    # изображение пасхалки
    egg_lbl = Label(image=egg_image)
    egg_lbl.place(x="80", y="0")
