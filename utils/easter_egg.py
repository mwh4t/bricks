from tkmacosx import CircleButton
from utils.widget_operations import clear_widgets_func
from other.params import BACK_BTN_CONFIG
from utils.back_btn import back_btn_func


def easter_egg_func(game_title, profile_btn, start_btn, help_btn, stat_btn, main_img_lbl,
                    egg_lbl, back_btn_image):
    """
    Функция пасхалки
    """
    clear_widgets_func([game_title, profile_btn, start_btn, help_btn, stat_btn, main_img_lbl])

    # кнопка "назад"
    back_btn = CircleButton(image=back_btn_image, **BACK_BTN_CONFIG, command=lambda: back_btn_func(
        [back_btn, egg_lbl],
        {
            game_title: (270, 16),
            profile_btn: (760, 8),
            start_btn: (360, 128),
            help_btn: (357, 160),
            stat_btn: (348, 192),
            main_img_lbl: (460, 365)
        }
    )
                            )
    back_btn.place(x="8", y="8")

    egg_lbl.place(x="80", y="0")
