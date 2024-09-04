# Импортируем функцию choice из модуля random для случайного выбора элементов
from random import choice, seed

# Списки с русскими фамилиями, мужскими именами, женскими именами и отчествами
SURNAMES = ['Иванов', 'Петров', 'Сидоров', 'Пушкин', 'Селин', 'Морозов', 'Точилов', 'Смирнов', 'Калядин']
MALE_NAMES = ['Пётр', 'Иван', 'Михаил', 'Денис', 'Михаил']
FEMALE_NAMES = ['Анна', 'Юлия', 'Галина', 'Надежда', 'Ольга', 'Оксана']
PATRONYMIC = ['Иванов', 'Петров', 'Егоров', 'Григорьев', 'Андреев', 'Александров', 'Алексеев',
              'Гвидонов', 'Валерьев', 'Михайлов']
GENDERS = ['male', 'female']  # Массив с возможными половыми вариантами


def generate_name(surnames: list[str],
                  male_names: list[str],
                  female_names: list[str],
                  patronymic: list[str],
                  gender: str) -> tuple[str, str, str]:
    """
    Генерирует полное имя на основе предоставленных параметров.

    Args:
    surnames (list[str]): Список фамилий
    male_names (list[str]): Список мужских имен
    female_names (list[str]): Список женских имен
    patronymic (list[str]): Список отчеств
    gender (str): Пол человека ('male' или 'female')

    Returns:
    tuple[str, str, str]: Триплет с полной фамилией, именем и отчеством
    """
    # Выбирает случайную фамилию и добавляет окончание "а" для женщин
    full_surname = choice(surnames) + ('' if gender == 'male' else 'а')

    # Выбирает имя в соответствии с полом
    chosen_name = choice(male_names) if gender == 'male' else choice(female_names)

    # Выбирает отчество и добавляет окончание "ич" для мужчин или "на" для женщин
    full_patronymic = choice(patronymic) + ('ич' if gender == 'male' else 'на')

    return full_surname, chosen_name, full_patronymic


def main() -> None:
    """
    Основная функция, которая генерирует и выводит 10 случайных имен.
    """
    seed()
    for _ in range(10):
        print(' '.join(generate_name(SURNAMES, MALE_NAMES, FEMALE_NAMES, PATRONYMIC, choice(GENDERS))))


if __name__ == '__main__':
    main()