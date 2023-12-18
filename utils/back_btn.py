def back_btn_func(hide_widgets):
    """
    Функция кнопки "назад"
    """
    for widget in hide_widgets:
        widget.place_forget()
