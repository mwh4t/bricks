from tkinter import *
from tkmacosx import Button, CircleButton
from utils.profile.profile_btn import profile_btn_func
from utils.help_btn import help_btn_func
from utils.leaderboard_btn import leaderboard_btn_func
from utils.start_btn import start_btn_func
from utils.authorization import authorization_func
from utils.gh_btn import gh_btn_func
from utils.easter_egg import easter_egg_func
from other.params import CIRCLE_BTN_CONFIG, BTN_CONFIG, TITLE_CONFIG, EASTER_EGG_CONFIG
import json


def main_menu_func(root):
    """
    Функция главного меню
    """
    # открытие json-файла
    with open("other/constants.json", 'r') as json_file:
        const = json.load(json_file)
        print(f"Статус авторизации: {const.get('authorization')}")

    # изображение кнопки "назад"
    back_btn_image = PhotoImage(file="other/images/back.png")
    w_back_btn_image = PhotoImage(file="other/images/w_back.png")

    # название игры
    game_title = Label(text='Игра "Кирпичи"', **TITLE_CONFIG)
    game_title.place(x="270", y="16")

    # изображение кнопки для изменения почты, логина и пароля
    settings_image = PhotoImage(file="other/images/settings.png")
    w_settings_image = PhotoImage(file="other/images/w_settings.png")

    # кнопка "профиль"
    profile_btn_image = PhotoImage(file="other/images/profile.png")
    w_profile_btn_image = PhotoImage(file="other/images/w_profile.png")
    profile_btn = CircleButton(image=profile_btn_image, **CIRCLE_BTN_CONFIG,
                               activeimage=w_profile_btn_image,
                               command=lambda: profile_btn_func(
                                   root, settings_image, w_settings_image, profile_btn, game_title, start_btn, help_btn,
                                   leaderboard_btn, gh_btn, main_img_btn, back_btn_image, w_back_btn_image))
    profile_btn.place(x="760", y="8")

    # кнопка "начать"
    if const.get("authorization") is True:
        start_btn = Button(text="Начать", **BTN_CONFIG,
                           command=lambda: start_btn_func(
                               root, game_title, profile_btn, start_btn, help_btn, leaderboard_btn,
                               gh_btn, main_img_btn, back_btn_image, w_back_btn_image))
    else:
        start_btn = Button(text="Начать", **BTN_CONFIG,
                           command=lambda: authorization_func(
                               root, profile_btn, game_title, start_btn, help_btn,
                               leaderboard_btn, gh_btn, main_img_btn, back_btn_image, w_back_btn_image))
    start_btn.place(x="360", y="128")

    # кнопка "справка"
    help_btn = Button(text="Справка", **BTN_CONFIG,
                      command=lambda: help_btn_func(
                          root, game_title, profile_btn, start_btn, help_btn, leaderboard_btn,
                          gh_btn, main_img_btn, back_btn_image, w_back_btn_image))
    help_btn.place(x="357", y="160")

    # кнопка "таблица лидеров"
    leaderboard_btn = Button(text="Таблица\nлидеров", **BTN_CONFIG,
                             command=lambda: leaderboard_btn_func(root))
    leaderboard_btn.place(x="357", y="192")

    # изображение в меню
    main_image = PhotoImage(file="other/images/bricks.png")
    main_img_btn = Button(image=main_image, **EASTER_EGG_CONFIG,
                          command=lambda: easter_egg_func(
                              root, game_title, profile_btn, start_btn, help_btn, leaderboard_btn,
                              gh_btn, main_img_btn, egg_image, back_btn_image, w_back_btn_image))
    main_img_btn.place(x="460", y="365")

    # изображение пасхалки
    egg_image = PhotoImage(file="other/images/новодворская-кирпич.gif")

    # кнопка-ссылка на ГитХаб
    gh_image = PhotoImage(file="other/images/gh.png")
    w_gh_image = PhotoImage(file="other/images/w_gh.png")
    gh_btn = CircleButton(image=gh_image, activeimage=w_gh_image,
                          **CIRCLE_BTN_CONFIG, command=lambda: gh_btn_func())
    gh_btn.place(x="8", y="555")
