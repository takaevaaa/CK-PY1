salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

dox = salary * months
trat = 0

while months > 0: #траты
    months = months - 1
    trat = (spend * (1 + increase)**months) + trat

need_money = trat - dox

print(round(need_money))
