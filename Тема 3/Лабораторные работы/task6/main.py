list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_el = max(list_numbers)
max_el_in = list_numbers.index(max_el)
L = len(list_numbers)

list_numbers[max_el_in], list_numbers[L - 1] = list_numbers[L - 1], list_numbers[max_el_in]

print(list_numbers)
