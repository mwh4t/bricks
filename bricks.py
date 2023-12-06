from tkinter import *
from tkinter import messagebox
from tkmacosx import Button, CircleButton
from other.params import (BACK_BTN_CONFIG, BTN_CONFIG, TITLE_CONFIG, TEXT_CONFIG,
                          HELP_TEXT, EASTER_EGG_CONFIG)
import random

user_count = 0
pc_count = 0

def on_close():
    """
    Функция для закрытия окна игры
    """
    response = messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?")
    if response:
        root.destroy()

def back_btn_func(hide_widgets, show_widgets_coords):
    """
    Функция кнопки "назад"
    """
    for widget in hide_widgets:
        widget.place_forget()

    for widget, (x_coord, y_coord) in show_widgets_coords.items():
        widget.place(x=x_coord, y=y_coord)

# def lang_btn_func():
#     """
#     Функция кнопки "язык"
#     """
#     if lang_btn.image_num == 1:
#         lang_btn.configure(image=enlang_btn_image)
#
#         game_title.config(text='The game "Bricks"')
#         game_title.place(x="250", y="16")
#
#         start_btn.config(text="Start")
#
#         help_btn.config(text="Help")
#         help_btn.place(x="360", y="160")
#
#         stat_btn.config(text="Statistics")
#         stat_btn.place(x="358", y="192")
#
#         lang_btn.image_num = 2
#     else:
#         lang_btn.configure(image=rulang_btn_image)
#         lang_btn.image_num = 1

def profile_btn_func():
    """
    Функция кнопки "профиль"
    """
    profile_btn.place_forget()
    game_title.place_forget()
    start_btn.place_forget()
    help_btn.place_forget()
    stat_btn.place_forget()
    main_img_lbl.place_forget()

    # кнопка "назад"
    back_btn_image = PhotoImage(file="other/images/back.png")
    back_btn = CircleButton(image=back_btn_image, **BACK_BTN_CONFIG, command=lambda: back_btn_func(
        [back_btn],
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

def help_btn_func():
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
    back_btn_image = PhotoImage(file="other/images/back.png")
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

def stat_btn_func():
    """
    Функция кнопки "статистика"
    """
    def close_top(toplevel):
        """
        Функция закрытия окна статистики
        """
        toplevel.destroy()

    def save_stat():
        """
        Функция кнопки "сохранить"
        """
        with open("stat.txt", "w") as file:
            file.write(f"Вы выиграли {user_count} раз.\n"
                       f"Компьютер выиграл {pc_count} раз.")
        messagebox.showinfo("Сохранение...", "Статистика успешно сохранена!")

    global user_count, pc_count

    top = Toplevel(root)
    top.title("Статистика")
    top.geometry("+600+300")
    top.resizable(False, False)
    top.configure(bg="#0e1620")

    # установка top как дочернего окна root
    top.transient(root)

    label = Label(top, text=f"Вы выиграли {user_count} раз.\n"
                            f"Компьютер выиграл {pc_count} раз.", **TEXT_CONFIG)
    label.pack(padx=8, pady=8)

    ok_btn = Button(top, text="OК", **BTN_CONFIG, command=lambda: close_top(top))
    ok_btn.pack(side=LEFT, padx=8, pady=8)

    save_btn = Button(top, text="Сохранить", **BTN_CONFIG, command=save_stat)
    save_btn.pack(side=RIGHT, padx=8, pady=8)

    # установка фокуса на top
    top.grab_set()

    # ожидание закрытия top
    root.wait_window(top)

    # после закрытия top освобождение фокус
    root.grab_release()

def start_btn_func():
    """
    Функция кнопки "начать"
    """
    global user_count, pc_count

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
        start_btn.place(x="360", y="128")
        help_btn.place(x="357", y="160")
        stat_btn.place(x="348", y="192")
        main_img_lbl.place(x="460", y="365")

    def win_func():
        """
        Функция победы компьютера или пользователя
        """
        nonlocal user_turn_flag
        global user_count, pc_count

        user_turn.place_forget()
        bricks_enter.place_forget()
        pc_turn.place_forget()
        next_btn.place_forget()

        menu_btn.place(x="360", y="258")
        stat_btn.place(x="348", y="290")

        if user_turn_flag.get():
            pc_win.place(x="210", y="200")
            pc_count += 1
        else:
            user_win.place(x="280", y="200")
            user_count += 1

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

def easter_egg_func():
    """
    Функция пасхалки
    """
    game_title.place_forget()
    profile_btn.place_forget()
    start_btn.place_forget()
    help_btn.place_forget()
    stat_btn.place_forget()
    main_img_lbl.place_forget()

    # кнопка "назад"
    back_btn_image = PhotoImage(file="other/images/back.png")
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

# создание основного окна
root = Tk()
root.title("Кирпичи")
root.geometry("800x600")
root.geometry("+300+100")
root.resizable(False, False)

# цвет фона
root.configure(bg="#0e1620")

# обработчик закрытия окна
root.protocol("WM_DELETE_WINDOW", on_close)

# название игры
game_title = Label(text='Игра "Кирпичи"', **TITLE_CONFIG)
game_title.place(x="270", y="16")

# кнопка "язык"
# rulang_btn_image = PhotoImage(file="other/images/rulng.png")
# enlang_btn_image = PhotoImage(file="other/images/enlng.png")
# lang_btn = CircleButton(image=rulang_btn_image, **BACK_BTN_CONFIG, command=lambda: lang_btn_func())
# lang_btn.image_num = 1 # дополнительный атрибут для отслеживания текущего изображения
# lang_btn.place(x="760", y="8")

# кнопка "профиль"
profile_btn_image = PhotoImage(file="other/images/profile.png")
profile_btn = CircleButton(image = profile_btn_image, **BACK_BTN_CONFIG, command=lambda: profile_btn_func())
profile_btn.place(x="760", y="8")

# кнопка "начать"
start_btn = Button(text="Начать", **BTN_CONFIG, command=start_btn_func)
start_btn.place(x="360", y="128")

# кнопка "справка"
help_btn = Button(text="Справка", **BTN_CONFIG, command=help_btn_func)
help_btn.place(x="357", y="160")

# кнопка "статистика"
stat_btn = Button(text="Статистика", **BTN_CONFIG, command=stat_btn_func)
stat_btn.place(x="348", y="192")

# изображение в меню
main_image = PhotoImage(file="other/images/bricks.png")
main_img_lbl = Button(image=main_image, **EASTER_EGG_CONFIG, command=easter_egg_func)
main_img_lbl.place(x="460", y="365")

# пасхалка
egg_image = PhotoImage(file="other/images/новодворская-кирпич.gif")
egg_lbl = Label(image=egg_image)

# запуск основного цикла
root.mainloop()
