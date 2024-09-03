def add_task_to_list(tasks):
    enter_task = input("Введите описание задачи:\n")
    tasks.append(enter_task)


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
            break
        elif enter == '1':
           add_task_to_list(tasks)
        elif enter == '2':
            index_task = int(input("Введите список по номеру для удаления задачи:\n"))
            tasks.remove(tasks[index_task])
        elif enter == '3':
            for i, item in enumerate(tasks):
                print(f"[{i}]: {item}")
        else:
            print("Вы вели что-то не так. Еще разок.")


if __name__ == '__main__':
    main()