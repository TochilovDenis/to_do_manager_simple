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
    with open(filename, 'r', encoding='utf-8') as file:
        return [task.strip() for task in file.readlines()]