# TODO решить с помощью list comprehension и распечатать его
import pprint

a = []
i = 0

while i < 16:
    temp = {'bin': bin(i), 'oct': oct(i), 'dec': i, 'hex': hex(i)}
    a.append(temp)
    i = i + 1

pprint.pprint(a)
