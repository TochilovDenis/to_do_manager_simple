""" Модуль для функций разбора дат """

from datetime import datetime

FORMATS: list = ["%Y-%m-%d", "%Y/%m/%d"]

def is_date_by_format(date: str, format_date: str) -> bool:
    """
    Функция для проверки того, является ли строка датой в соответствии с форматом
    :param date: строка, представляющая дату
    :return: True, если строка является датой в соответствии с форматом, else False
    """
    try:
        datetime.strptime(date, format_date)
        return True
    except ValueError:
        return False


def is_date(date: str) -> bool:
    for format_date in FORMATS:
        if is_date_by_format(date, format_date):
            return True
    return False