from main import print_list_of_task

def test_print_list_of_task_empty(capsys):
    tasks = []
    print_list_of_task(tasks)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Список задач пуст"