# Импортируем функцию choice из модуля random для случайного выбора элементов
from random import choice, seed

# для записи в файл
FILENAME = 'names.txt'

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


def formats_string(names: tuple[str, str, str]) -> str:
    """
    Принимает кортеж строк и форматирует его в одну строку,
    разделенную пробелами и заканчивающуюся символом \n
    :param names:
    :return:
    """
    return ':'.join(names) + '\n'


def write_names(filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        for _ in range(10):
            names = generate_name(SURNAMES, MALE_NAMES, FEMALE_NAMES, PATRONYMIC, choice(GENDERS))
            file.write(formats_string(names))


def read_names(filename: str) -> None:
    with open(filename, 'r', encoding='utf-8') as file:
        read_names = file.readlines()
        print(''.join(read_names))
        print(f"Количество сохраненных строк: {len(read_names)}")


def read_names_index(filename: str, index: int) -> None:
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for l in lines:
            if 0 <= index < len(l.split(":")):
                print(l.split(":")[index])
            else:
                print("Unknown")
                break


def main() -> None:
    """
    Основная функция, которая генерирует и выводит 10 случайных имен.
    """
    seed()

    write_names(FILENAME)
    read_names(FILENAME)
    read_names_index(FILENAME, 1)

if __name__ == '__main__':
    main()