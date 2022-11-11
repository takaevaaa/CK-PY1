import random

def get_unique_list_numbers() -> list[int]:

    numbers = []
    i = 0
    while len(numbers) < 15:
        i = i + 1
        n = random.randint(-10, 10)
        if n not in numbers:
            numbers.append(n)
    return numbers
# TODO написать функцию для получения списка уникальных целых чисел

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
