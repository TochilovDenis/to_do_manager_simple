FILENAME = 'file.txt'

def generate_list() -> list[str]:
    """
    Функция для создания списка строк из целочисленного диапазона от 0 до 50
    :return: a list of strings [компрехенсия список]
    """
    return [str(i) + '\n' for i in range(1, 50)]

def write_to_file(list_to_write: list[str], filename: str) -> None:
    """
    Функция для записи списка строк в файл с именем filename
    :param list_to_write:  список строк для записи в файл
    :param filename: в какой файл записывать список
    :return: nothing
    """
    with open(filename, 'w') as file:
        file.writelines(list_to_write)

def read_from_file(filename: str) -> list[str]:
    """
    Функция для чтения списка строк из файла с именем filename
    :param filename: имя файла для чтения
    :return: list of strings
    """
    with open(filename, 'r') as file:
        result = file.readlines()
    return result

def print_list(list_to_print: list[str]) -> None:
    """
    Функция для печати списка строк
    :param list_to_print: список для печати
    :return: nothing
    """
    for el in list_to_print:
        print(el, end='')

def main() -> None:
    """
    Основная функция
    :return: nothing
    """
    l: list[str] = generate_list()
    write_to_file(l, FILENAME)
    new_list = read_from_file(FILENAME)
    print_list(new_list)

if __name__ == '__main__':
    main()
