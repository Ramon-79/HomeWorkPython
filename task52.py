def premia(name, cash, percent):
    """
    Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
    имена str, ставка int, премия str с указанием процентов вида «10.25%».
    В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
    Сумма рассчитывается как ставка умноженная на процент премии.
    :param names:
    :param cash:
    :param percent:
    :return:
    """
    return {name: money / 100 * perc
            for name, money, perc in zip(name, cash, (float(i[:-1]) for i in percent))}



name = ["Name1", "Name2", "Name3"]
cash = [222, 111, 444]
percent = ["19.5%", "75.00%", "44.44%"]
print(premia(name, cash, percent))
