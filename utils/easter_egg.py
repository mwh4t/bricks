from tkmacosx import CircleButton
from utils.widget_operations import clear_widgets_func
from other.params import BACK_BTN_CONFIG
from utils.back_btn import back_btn_func


def easter_egg_func(root, game_title, profile_btn, start_btn, help_btn,
                    stat_btn, main_img_lbl, egg_lbl, back_btn_image):
    """
    Функция пасхалки
    """
    clear_widgets_func([game_title, profile_btn, start_btn,
                        help_btn, stat_btn, main_img_lbl])

    # кнопка "назад"
    from utils.main_menu import main_menu_func
    back_btn = CircleButton(image=back_btn_image, **BACK_BTN_CONFIG,
                            command=lambda: (back_btn_func(
                                [back_btn, egg_lbl]), main_menu_func(root)))
    back_btn.place(x="8", y="8")

    egg_lbl.place(x="80", y="0")
