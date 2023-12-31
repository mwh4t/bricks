# параметры для кнопок
BTN_CONFIG = {
    "bg": "#1e2c3a",
    "activebackground": "#1e2c3a",
    "overbackground": "#23303e",
    "font": "Helvetica 16",
    "fg": "white",
    "borderless": True,
    "focusthickness": 0,
}

# параметры для круглых кнопок
CIRCLE_BTN_CONFIG = {
    "width": 32,
    "bg": "#0e1620",
    "activebackground": "#0e1620",
    "borderless": True,
    "bd": 0,
    "focusthickness": 0,
    "highlightthicknes": 0,
    "overbackground": "#0e1620"
}

# параметры для радиокнопок
RB_CONFIG = {
    "bg": "#0e1620",
    "activebackground": "#0e1620",
    "font": "Helvetica 16",
    "activeforeground": "#D8D5E2",
    "bd": 0
}

# параметры для кнопки "регистрация"
REG_BTN = {
    "width": 90,
    "height": 18,
    "bg": "#0e1620",
    "bd": 5,
    "activebackground": "#0e1620",
    "overforeground": "#D8D5E2",
    "font": "Helvetica 16",
    "fg": "white",
    "borderless": True
}

# параметры для заголовков
TITLE_CONFIG = {
    "font": "Helvetica 36 bold",
    "fg": "white",
    "bg": "#0e1620",
    "justify": "center"
}

# параметры для текстов
TEXT_CONFIG = {
    "font": "Helvetica 16",
    "fg": "white",
    "bg": "#0e1620",
    "highlightthickness": 0
}

# текст правил
HELP_TEXT = {
    "text": '• Игра начинается со случайного задания количества кирпичей (от 12 до 20).\n\n'
            '• Игроки ходят поочередно:\n\n'
            '   • сначала пользователь,\n\n'
            '   • затем компьютер.\n\n'
            '• В каждом ходе игрок может выбрать от 1 до 3 кирпичей.\n\n'
            '• Проигрывает тот игрок, который не может сделать ход из-за отсутствия кирпичей.\n\n'
            '• Игра сохраняет статистику:\n\n'
            '   • количество сыгранных игр,\n\n'
            '   • побед и поражений для каждого игрока.\n\n'
            '• Возможность просмотра статистики после каждой игры.\n\n'
            '• Возможность сохранения статистики для последующего просмотра.\n\n'
            '• В начале каждой игры отображается количество кирпичей.\n\n'
            '• Возможность начать новую игру после завершения предыдущей.\n\n'
            '• Возможность вернуться в главное меню после начала игры.\n\n'
            '• Уведомление об окончании игры и показ победителя.'
}

# параметры для пасхалки
EASTER_EGG_CONFIG = {
    "width": 350,
    "height": 250,
    "bg": "#0e1620",
    "bd": 3,
    "activebackground": "#0e1620",
    "overbackground": "#0e1620",
    "borderless": True,
    "focusthickness": 0
}
