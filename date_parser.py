""" Модуль для функций разбора дат """

from datetime import datetime

def is_date(date: str) -> bool:
    """
    Функция для проверки того, является ли строка датой в соответствии с форматом
    :param date: строка, представляющая дату
    :return: True, если строка является датой в соответствии с форматом, else False
    """
    template = '%Y-%m-%d'
    try:
        datetime.strptime(date, template)
        return True
    except ValueError:
        return False
