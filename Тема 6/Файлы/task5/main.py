INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    ...  # TODO перезаписать содержимое одного файла в другой


task()

with open(OUTPUT_FILE) as file:
    for line in file:
        print(line, end="")
