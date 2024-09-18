from errors import NoMoreAttempts, RefuseToCreateNewUser
from files import read_tasks_file,save_tasks_file
from get_user import get_user
from tasks import tasks_process


FILENAME = "tasks.txt"
FILENAME_USER = 'user.txt'


def main() -> None:
    """
    Main function
    :return: nothing
    """
    # Объявляем список задач
    tasks = read_tasks_file(FILENAME)
    try:
        # Проверка пользователя
        get_user(FILENAME_USER)
        # Главный цикл
        tasks_process(tasks)
    except (NoMoreAttempts, RefuseToCreateNewUser) as e:
        print(f"Ошибка: {e}")
    finally:
        save_tasks_file(tasks, FILENAME)


if __name__ == '__main__':
    main()