from unittest.mock import patch

from main import print_list_of_task, add_task_to_list

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


@patch('builtins.input')
def test_add_task_to_list(mock_input):
    mock_input.return_value = "task-01"
    tasks = []
    add_task_to_list(tasks)
    assert tasks[0] == 'task-01'