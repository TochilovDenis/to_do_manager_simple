""" Модуль для функций разбора дат """
from datetime import datetime

def is_date(date: str) -> bool:
    template = '%Y-%m-%d'
    try:
        datetime.strptime(date, template)
        return True
    except ValueError:
        return False
