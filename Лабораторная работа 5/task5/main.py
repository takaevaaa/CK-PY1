import random
import string


# генерируетя пароль из НЕповторяющихся символов, максимальная длина пароля - 62 символа


# def get_random_password(k) -> str:
#     alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
#     x = random.sample(alphabet, k)
#     password = "".join(x)
#     return password
#
#
# print(get_random_password(8))


# генерируетя пароль из повторяющихся символов, максимальная длина пароля - любая


def get_random_password(k) -> str:
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = " "
    i = 0
    while i < k:
        i = i + 1
        new_symbol = "".join(random.sample(alphabet, 1))
        password = password + new_symbol

    return password


print(get_random_password(63))
