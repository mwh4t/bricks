from tkinter import *
from tkmacosx import Button, CircleButton
from utils.close import close_func
from utils.profile_btn import profile_btn_func
from utils.help_btn import help_btn_func
from utils.stat_btn import stat_btn_func
from utils.start_btn import start_btn_func
from utils.easter_egg import easter_egg_func
from other.params import BACK_BTN_CONFIG, BTN_CONFIG, TITLE_CONFIG, EASTER_EGG_CONFIG

authorization = False
user_count = 0
pc_count = 0


# создание основного окна
root = Tk()
root.title("Кирпичи")
root.geometry("800x600")
root.geometry("+300+100")
root.resizable(False, False)

# цвет фона
root.configure(bg="#0e1620")

# изображение кнопки "назад"
back_btn_image = PhotoImage(file="other/images/back.png")

# обработчик закрытия окна
root.protocol("WM_DELETE_WINDOW", lambda: close_func(root))

# название игры
game_title = Label(text='Игра "Кирпичи"', **TITLE_CONFIG)
game_title.place(x="270", y="16")

# кнопка "профиль"
profile_btn_image = PhotoImage(file="other/images/profile.png")
profile_btn = CircleButton(image=profile_btn_image, **BACK_BTN_CONFIG, command=lambda: profile_btn_func(
    profile_btn, game_title, start_btn, help_btn, stat_btn, main_img_lbl, authorization, back_btn_image))
profile_btn.place(x="760", y="8")

# кнопка "начать"
if authorization:
    start_btn = Button(text="Начать", **BTN_CONFIG, command=lambda: start_btn_func(
        game_title, profile_btn, start_btn, help_btn, stat_btn, main_img_lbl, back_btn_image))
else:
    start_btn = Button(text="Начать", **BTN_CONFIG, command=lambda: profile_btn_func(
        profile_btn, game_title, start_btn, help_btn, stat_btn, main_img_lbl, authorization, back_btn_image))
start_btn.place(x="360", y="128")

# кнопка "справка"
help_btn = Button(text="Справка", **BTN_CONFIG, command=lambda: help_btn_func(
    game_title, profile_btn, start_btn, help_btn, stat_btn, main_img_lbl, back_btn_image))
help_btn.place(x="357", y="160")

# кнопка "статистика"
stat_btn = Button(text="Статистика", **BTN_CONFIG, command=lambda: stat_btn_func(root, user_count, pc_count))
stat_btn.place(x="348", y="192")

# изображение в меню
main_image = PhotoImage(file="other/images/bricks.png")
main_img_lbl = Button(image=main_image, **EASTER_EGG_CONFIG, command=lambda: easter_egg_func(
    game_title, profile_btn, start_btn, help_btn, stat_btn, main_img_lbl, egg_lbl, back_btn_image))
main_img_lbl.place(x="460", y="365")

# пасхалка
egg_image = PhotoImage(file="other/images/новодворская-кирпич.gif")
egg_lbl = Label(image=egg_image)

# запуск основного цикла
root.mainloop()
