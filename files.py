import os


def write_to_file(list_to_write: list[str], filename: str) -> None:
    """
    Функция для записи списка строк в файл с именем filename
    :param list_to_write:  список строк для записи в файл
    :param filename: в какой файл записывать список
    :return: nothing
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines('\n'.join(list_to_write))


def read_from_file(filename: str) -> list[str]:
    """
    Функция для чтения списка строк из файла с именем filename
    :param filename: имя файла для чтения
    :return: list of strings
    """
    with open(filename, 'r') as file:
        result = file.readlines()
    return result


def save_tasks_file(list_of_tasks: list[str],filename:str ) -> None:
    """
    Функция для записи списка задач в файл с именем filename
    :param list_of_tasks:  список задачи для записи в файл
    :param filename: в какой файл записывать список
    :return: nothing
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(list_of_tasks))


def read_tasks_file(filename: str) -> list[str]:
    """
    Читает список задач из текстового файла и возвращает его как список строк.

    Проверяет наличие файла перед чтением. Если файл не существует,
    возвращает пустой список.

    :param filename: Имя файла, из которого нужно прочитать задачи.
                     Путь к файлу должен быть абсолютным или относительным.
    :return: Список строковых задач, считанных из файла.
             Если файл не существует, возвращается пустой список.
    :raises FileNotFoundError: Если указанный файл не существует.
    """
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as file:
        return [task.strip() for task in file.readlines()]



def read_users_file(filename:str) -> dict[str, str]:
    result: dict[str, str] = {}
    if not os.path.exists(filename):
        return result

    with open(filename, 'r', encoding='utf-8') as file:
        return {line.split(":")[0].strip() : line.split(":")[1].strip() for line in file.readlines()}


def add_users_file(filename: str, user: str, password: str) -> None:
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"{user}: {password}\n")
