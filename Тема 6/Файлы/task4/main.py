OUTPUT_FILE = "output.txt"


def task():
    ...  # TODO записать одну строку с квадратами целых чисел в файл


task()

with open(OUTPUT_FILE) as file:
    for line in file:
        print(line, end="")
