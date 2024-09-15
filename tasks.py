from date_parser import is_date_any, FORMATS


def add_task_to_list(list_of_tasks: list[str]) -> None:
    """
    Добавить задачу в список задач
    :param list_of_tasks: list of tasks to add a task to
    :return: Nothing
    """
    enter_task = input("Введите описание задачи:\n")
    attempts = 5
    for _ in range(attempts):
        enter_data = input(f"Введите срок задачи {FORMATS}:\n")
        if is_date_any(enter_data):
            enter = f"{enter_task}:{enter_data}"
            list_of_tasks.append(enter)
            print("OK")
            break
        else:
            print("Error format dat!!!")
    else:
        print("Вы исчерпали все возможные попытки. Задача не будет добавлена.")


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
            enter_task, enter_data = item.split(":")
            print(f"[{i}]: Задача: {enter_task} | Срок: {enter_data}")
    else:
        print("Список задач пуст")


def tasks_process(tasks) -> None:
    while True:
        print("1. Добавить задачу\n"
              "2. Удалить задачу\n"
              "3. Вывести список всех задач\n"
              "4. Выход")
        enter = input("Введите ваш выбор: ")
        if enter == '4':
            print("Программа завершена.")
            break
        elif enter == '1':
            add_task_to_list(tasks)
        elif enter == '2':
            delete_task_from_list(tasks)
        elif enter == '3':
            print_list_of_task(tasks)
        else:
            print("Вы вели что-то не так. Еще разок.")
