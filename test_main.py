from main import print_list_of_task

def test_print_list_of_task_empty(capsys):
    tasks = []
    print_list_of_task(tasks)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Список задач пуст"


def test_print_list_of_task_not_empty(capsys):
    tasks = []
    tasks.append("task-01")
    print_list_of_task(tasks)
    captured = capsys.readouterr()
    assert captured.out.strip() == "[0]: task-01"