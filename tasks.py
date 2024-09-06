from files import write_to_file
FILE_PATH = "tasks.txt"

def add_task_to_list(list_of_tasks: list[str]) -> None:
    """
    Добавить задачу в список задач
    :param list_of_tasks: list of tasks to add a task to
    :return: Nothing
    """
    enter_task = input("Введите описание задачи:\n")
    list_of_tasks.append(enter_task)


def delete_task_from_list(list_of_tasks: list[str]) -> None:
    """
    Удаление задачи из списка задач
    :param list_of_tasks: list of tasks to delete from
    :return: Nothing
    """
    # Проверяем если список задач пуст
    if not list_of_tasks:
        print("Список пуст!")
        return

    index = input("Введите список по номеру для удаления задачи:\n")
    # Проверяем является ли индекс вообще числом
    if not index.isalnum():
        print("Ошибка | Нужно было ввести целое число")
        return
    # Превращаем из str в int
    index = int(index)
    # Проверяем попадает ли индекс в диапазон количества элементов
    if not 0 <= index < len(list_of_tasks):
        print("Ошибка | Вы ввели неправильное число")
        return

    list_of_tasks.remove(list_of_tasks[index])


def print_list_of_task(list_to_print: list[str]) -> None:
    """
    Функция для вывода на печать списка задач
    :param list_to_print: list of tasks to print
    :return: Nothing
    """
    if list_to_print:
        for i, item in enumerate(list_to_print):
            print(f"[{i}]: {item}")
    else:
        print("Список задач пуст")


def main() -> None:
    tasks = []
    while True:
        print("1. Добавить задачу\n"
              "2. Удалить задачу\n"
              "3. Вывести список всех задач\n"
              "4. Выход")
        enter = input("Введите ваш выбор: ")
        if enter == '4':
            print("Программа завершена.")
            write_to_file(tasks, FILE_PATH)
            break
        elif enter == '1':
            add_task_to_list(tasks)
        elif enter == '2':
            delete_task_from_list(tasks)
        elif enter == '3':
            print_list_of_task(tasks)
        else:
            print("Вы вели что-то не так. Еще разок.")


if __name__ == '__main__':
    main()
