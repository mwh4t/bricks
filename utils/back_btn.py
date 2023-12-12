def back_btn_func(hide_widgets, show_widgets_coords):
    """
    Функция кнопки "назад"
    """
    for widget in hide_widgets:
        widget.place_forget()

    for widget, (x_coord, y_coord) in show_widgets_coords.items():
        widget.place(x=x_coord, y=y_coord)
