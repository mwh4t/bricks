from tkinter import *
from tkmacosx import CircleButton
from utils.widget_operations import clear_widgets_func
from other.params import BACK_BTN_CONFIG, TITLE_CONFIG, TEXT_CONFIG, HELP_TEXT
from utils.back_btn import back_btn_func


def help_btn_func(root, game_title, profile_btn, start_btn, help_btn,
                  stat_btn, main_img_lbl, back_btn_image):
    """
    Функция кнопки "справка"
    """
    clear_widgets_func([game_title, profile_btn, start_btn,
                        help_btn, stat_btn, main_img_lbl])

    # кнопка "назад"
    from utils.main_menu import main_menu_func
    back_btn = CircleButton(image=back_btn_image, **BACK_BTN_CONFIG,
                            command=lambda: (back_btn_func(
                                [help_title, help_text, help_scrollbar, back_btn]),
                                             main_menu_func(root)))
    back_btn.place(x="8", y="8")

    # название страницы "справка"
    help_title = Label(text="Справка", **TITLE_CONFIG)
    help_title.place(x="320", y="16")

    # текст правил
    help_text = Text(**TEXT_CONFIG)
    help_text.insert("1.0", HELP_TEXT["text"])

    # scrollbar для текста правил
    help_scrollbar = Scrollbar(command=help_text.yview)
    help_scrollbar.place(x="785", y="0", relheight=1)

    help_text.config(state=DISABLED, selectbackground="#0e1620",
                     yscrollcommand=help_scrollbar.set)
    help_text.place(x="40", y="100")
