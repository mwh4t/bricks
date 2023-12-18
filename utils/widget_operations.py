from tkinter import *


def clear_widgets_func(widgets):
    """
    Функция для очистки всех виджетов
    """
    for widget in widgets:
        widget.place_forget()


def clear_entries_func(entries):
    """
    Функция для очистки полей ввода
    """
    for entry in entries:
        entry.delete(0, "end")


def clear_rb_func(rbs):
    """
    Функция для очистки значений радиокнопок
    """
    for rb in rbs:
        rb.set(NONE)
