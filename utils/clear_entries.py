def clear_entries_func(entries):
    """
    Функция для очистки полей ввода
    """
    for entry in entries:
        entry.delete(0, 'end')
