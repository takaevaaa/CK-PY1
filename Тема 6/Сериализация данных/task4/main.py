import json

INPUT_FILE = "input.json"
OUTPUT_FILE = "output.json"


def task() -> None:
    ...  # TODO считать содержимое файла из аргумента input_filename

    ...  # TODO записать содержимое в файл из аргумента output_filename


task()

with open(OUTPUT_FILE) as output_f:
    for line in output_f:
        print(line, end="")
