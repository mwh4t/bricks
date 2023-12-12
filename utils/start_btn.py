import random
from tkinter import *
from tkinter import messagebox
from tkmacosx import Button, CircleButton
from other.params import TITLE_CONFIG, BACK_BTN_CONFIG, BTN_CONFIG, TEXT_CONFIG
from utils.back_btn import back_btn_func


def start_btn_func(game_title, profile_btn, start_btn, help_btn, stat_btn, main_img_lbl):
    """
    Функция кнопки "начать"
    """
    game_title.place_forget()
    profile_btn.place_forget()
    start_btn.place_forget()
    help_btn.place_forget()
    stat_btn.place_forget()
    main_img_lbl.place_forget()

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
                        bricks_enter.delete(0, END)

                    else:
                        messagebox.showwarning("Ошибка", "Количество кирпичей должно быть от 1 до 3.")
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
            back_btn.place_forget()
            bricks_num.place_forget()
            pc_turn.place_forget()

            user_turn.place(x="320", y="190")
            bricks_enter.place(x="310", y="250")
        else:
            win_func()

    def pc_turn_func():
        """
        Функция хода компьютера
        """
        nonlocal bricks_num_rand, pc_turn_var

        back_btn.place_forget()
        bricks_num.place_forget()
        user_turn.place_forget()
        bricks_enter.place_forget()

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
        bricks_num1.place_forget()
        menu_btn.place_forget()
        stat_btn.place_forget()
        pc_win.place_forget()
        user_win.place_forget()

        game_title.place(x="270", y="16")
        profile_btn.place(x="760", y="8")
        start_btn.place(x="360", y="128")
        help_btn.place(x="357", y="160")
        stat_btn.place(x="348", y="192")
        main_img_lbl.place(x="460", y="365")

    def win_func():
        """
        Функция победы компьютера или пользователя
        """
        nonlocal user_turn_flag
        # global user_count, pc_count

        user_turn.place_forget()
        bricks_enter.place_forget()
        pc_turn.place_forget()
        next_btn.place_forget()

        menu_btn.place(x="360", y="258")
        stat_btn.place(x="348", y="290")

        if user_turn_flag.get():
            pc_win.place(x="210", y="200")
            # pc_count += 1
        else:
            user_win.place(x="280", y="200")
            # user_count += 1

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
    back_btn_image = PhotoImage(file="other/images/back.png")
    back_btn = CircleButton(image=back_btn_image, **BACK_BTN_CONFIG, command=lambda: back_btn_func(
        [back_btn, next_btn, bricks_num, user_turn, bricks_enter],
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

    # кнопка "далее"
    next_btn = Button(text="Далее", **BTN_CONFIG, command=next_btn_func)
    next_btn.place(x="360", y="558")

    # текст с количеством кирпичей
    bricks_num = Label(text=f"Количество кирпичей:\n{bricks_num_rand}", **TITLE_CONFIG)
    bricks_num.place(x="200", y="16")

    # число кирпичей в углу
    bricks_num1 = Label(text="", **TEXT_CONFIG)
    bricks_num1.place()

    # текст с выйгрышем компьютера
    pc_win = Label(text="Компьютер выиграл!", **TITLE_CONFIG)
    pc_win.place()

    # текст с выйгрышем пользователя
    user_win = Label(text="Вы выиграли!", **TITLE_CONFIG)
    user_win.place()

    # кнопка "меню"
    menu_btn = Button(text="Меню", **BTN_CONFIG, command=lambda: menu_btn_func())
    menu_btn.place()
