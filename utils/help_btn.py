from tkinter import *
from tkmacosx import CircleButton
from other.params import BACK_BTN_CONFIG, TITLE_CONFIG, TEXT_CONFIG, HELP_TEXT
from utils.back_btn import back_btn_func


def help_btn_func(game_title, profile_btn, start_btn, help_btn, stat_btn, main_img_lbl, back_btn_image):
    """
    Функция кнопки "справка"
    """
    game_title.place_forget()
    profile_btn.place_forget()
    start_btn.place_forget()
    help_btn.place_forget()
    stat_btn.place_forget()
    main_img_lbl.place_forget()

    # кнопка "назад"
    back_btn = CircleButton(image=back_btn_image, **BACK_BTN_CONFIG, command=lambda: back_btn_func(
        [help_title, help_text, help_scrollbar, back_btn],
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

    # название страницы "справка"
    help_title = Label(text="Справка", **TITLE_CONFIG)
    help_title.place(x="320", y="16")

    # текст правил
    help_text = Text(**TEXT_CONFIG)
    help_text.insert("1.0", HELP_TEXT["text"])

    # scrollbar для текста правил
    help_scrollbar = Scrollbar(command=help_text.yview)
    help_scrollbar.place(x="785", y="0", relheight=1)

    help_text.config(state=DISABLED, selectbackground="#0e1620", yscrollcommand=help_scrollbar.set)
    help_text.place(x="40", y="100")
