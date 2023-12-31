import random
from tkinter import *
from tkinter import messagebox
from tkmacosx import Button, CircleButton
from utils.widget_operations import clear_widgets_func, clear_entries_func
from other.params import TITLE_CONFIG, CIRCLE_BTN_CONFIG, BTN_CONFIG, TEXT_CONFIG
from utils.back_btn import back_btn_func
from utils.stat_btn import stat_btn_func
import json


def start_btn_func(root, game_title, profile_btn, start_btn, help_btn, leaderboard_btn,
                   gh_btn, main_img_btn, back_btn_image, w_back_btn_image):
    """
    Функция кнопки "начать"
    """
    # открытие json-файлов
    with open("other/constants.json", 'r') as json_file1:
        const = json.load(json_file1)
    with open("db.json", 'r') as json_file:
        reg_data = json.load(json_file)

    clear_widgets_func([game_title, profile_btn, start_btn, help_btn,
                        leaderboard_btn, gh_btn, main_img_btn])

    bricks_num_rand = random.randint(12, 20)

    user_turn_flag = BooleanVar(value=False)

    def next_btn_func():
        """
        Функция кнопки "далее"
        """
        nonlocal bricks_num_rand, user_turn_flag

        btn_state = user_turn_flag.get()
        user_turn_flag.set(not btn_state)

        # логика игры
        if user_turn_flag.get():
            user_turn_func()

            bricks_num1.config(text=f"{bricks_num_rand}")
            bricks_num1.place(x="770", y="8")
        else:
            if bricks_num_rand > 0:
                try:
                    user_bricks = int(bricks_enter.get())
                    if 1 <= user_bricks <= 3:
                        bricks_num_rand -= user_bricks
                        clear_entries_func([bricks_enter])

                    else:
                        messagebox.showwarning("Ошибка",
                                               "Количество кирпичей должно быть от 1 до 3.")
                        return
                    print(f"Ост. от юзера: {bricks_num_rand}")
                except ValueError:
                    return
            else:
                win_func()

            pc_turn_func()

            bricks_num1.config(text=f"{bricks_num_rand}")
            bricks_num1.place(x="770", y="8")

    def user_turn_func():
        """
        Функция хода пользователя
        """
        nonlocal bricks_num_rand

        if bricks_num_rand > 0:
            clear_widgets_func([back_btn, bricks_num, pc_turn])

            user_turn.place(x="320", y="190")
            bricks_enter.place(x="310", y="250")
        else:
            win_func()

    def pc_turn_func():
        """
        Функция хода компьютера
        """
        nonlocal bricks_num_rand, pc_turn_var

        clear_widgets_func([back_btn, bricks_num, user_turn, bricks_enter])

        if bricks_num_rand > 0:
            pc_turn_var = random.randint(1, 3)
            pc_turn.config(text=f"Ход компьютера:\n{pc_turn_var}")
            pc_turn.place(x="250", y="200")

            bricks_num_rand -= pc_turn_var
            print(f"Ост. от ПК: {bricks_num_rand}")
        else:
            win_func()

    def menu_btn_func():
        """
        Функция кнопки "меню"
        """
        clear_widgets_func([bricks_num1, stat_btn, menu_btn, pc_win, user_win])

        main_menu_func(root)

    def win_func():
        """
        Функция победы компьютера или пользователя
        """
        nonlocal user_turn_flag

        clear_widgets_func([user_turn, bricks_enter, pc_turn, next_btn])

        menu_btn.place(x="360", y="258")

        stat_btn.place(x="348", y="290")

        if user_turn_flag.get():
            pc_win.place(x="210", y="200")
            if const.get("current_username") in reg_data:
                reg_data[const["current_username"]]["pc_wins"] += 1
                with open("db.json", 'w') as file:
                    json.dump(reg_data, file, indent=4)
        else:
            user_win.place(x="280", y="200")
            if const.get("current_username") in reg_data:
                reg_data[const["current_username"]]["user_wins"] += 1
                with open("db.json", 'w') as file:
                    json.dump(reg_data, file, indent=4)

    # текст с ходом игрока
    user_turn = Label(text="Ваш ход:", **TITLE_CONFIG)
    user_turn.place()

    # поле ввода для игрока
    bricks_enter = Entry()
    bricks_enter.place()

    # текст с ходом компьютера
    pc_turn_var = random.randint(1, 3)
    pc_turn = Label(text=f"Ход компьютера:\n{pc_turn_var}", **TITLE_CONFIG)
    pc_turn.place()

    # кнопка "назад"
    from utils.main_menu import main_menu_func
    back_btn = CircleButton(image=back_btn_image, **CIRCLE_BTN_CONFIG,
                            activeimage=w_back_btn_image,
                            command=lambda: (back_btn_func(
                                [back_btn, next_btn, bricks_num, user_turn, bricks_enter]),
                                             main_menu_func(root)))
    back_btn.place(x="8", y="8")

    # кнопка "далее"
    next_btn = Button(text="Далее", **BTN_CONFIG,
                      command=next_btn_func)
    next_btn.place(x="360", y="558")

    # текст с количеством кирпичей
    bricks_num = Label(text=f"Количество кирпичей:\n{bricks_num_rand}", **TITLE_CONFIG)
    bricks_num.place(x="200", y="220")

    # число кирпичей в углу
    bricks_num1 = Label(text="", **TEXT_CONFIG)
    bricks_num1.place()

    # кнопка "статистика"
    stat_btn = Button(text="Статистика", **BTN_CONFIG,
                      command=lambda: stat_btn_func(root))

    # текст с выйгрышем компьютера
    pc_win = Label(text="Компьютер выиграл!", **TITLE_CONFIG)
    pc_win.place()

    # текст с выйгрышем пользователя
    user_win = Label(text="Вы выиграли!", **TITLE_CONFIG)
    user_win.place()

    # кнопка "меню"
    menu_btn = Button(text="Меню", **BTN_CONFIG,
                      command=lambda: menu_btn_func())
    menu_btn.place()
