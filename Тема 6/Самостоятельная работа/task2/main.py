# TODO импортировать необходимые молули


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла

    ...  # TODO записать список словарей в json файл


task()

with open(OUTPUT_FILENAME) as output_f:
    for line in output_f:
        print(line, end="")
