main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

def get_dict(strng):
    strng = strng.lower()
    dic = {}
    for i in strng:
        if i.isalpha():
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1
    return dic

def get_dict_in_per(strng):
    strng = strng.lower()
    dic = {}
    chars_counter = 0
    for i in strng:
        if i.isalpha():
            chars_counter += 1
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1

    for i in dic:
        dic[i] = (dic[i]/chars_counter)*100

    return dic


print(get_dict(main_str))
#print(get_dict_in_per(main_str))

