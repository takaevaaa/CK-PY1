import json


FILENAME = "input.json"


def task() -> list[dict]:
    with open(FILENAME) as f:
        json_data = json.load(f)

    ...  # TODO отсортировать и вернуть список словарей


data = task()
# TODO распечатать json строку отформатированную с отступами равными 4
