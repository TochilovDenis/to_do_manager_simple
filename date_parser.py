""" Модуль для функций разбора дат """

from datetime import datetime

FORMATS: list = ["%Y-%m-%d", "%Y/%m/%d"]

def is_date_by_format(date: str, format_date: str) -> bool:
    """
    Функция для проверки того, является ли строка датой в соответствии с форматом
    :param date: строка, представляющая дату
    :param format_date: строка, представляющая формат даты
    :return: True, если строка является датой в соответствии с форматом, else False
    """
    try:
        datetime.strptime(date, format_date)
        return True
    except ValueError:
        return False


def is_date(date: str) -> bool:
    """
    Функция для проверки, является ли дата строкой в соответствии со списком один формат из ФОРМАТОВ
    :param date: строка, представляющая дату
    :return: True - дата is_date_by одного формата из ФОРМАТОВ.
    """
    for format_date in FORMATS:
        if is_date_by_format(date, format_date):
            return True
    return False


def is_date_any(date: str) -> bool:
    """Простой вариант функции is_date_any"""
    return any([is_date_by_format(date, format_date) for format_date in FORMATS])