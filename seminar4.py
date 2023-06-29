import tinkoff as tn

def task41(*words):
    """
    Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
    Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся
    на s (кроме переменной из одной буквы s) на None.
    Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
    :param words:
    :return:
    """
    words = list(words)
    temp = []
    for i in range(len(words)):
        if words[i].endswith('s') and words[i] != 's':
            temp.append(words[i])
            words[i] = None
    print(words)
    print(temp)



# task41('sos', 'heh', 'соs', 's')
# help(task41)


def task42(*a_list: list[[int]]) -> list[()] | str:
    """
    Напишите функцию для транспонирования матрицы
    :param a_list:
    :return:
    """
    trans = True
    col = len(a_list[0])
    for a in list(a_list):
        if len(a) != col:
            trans = False
    if trans:
        return list(zip(*a_list))
    else:
        return 'Транспонирование невозможно'


# print(task42([1, 4, 7], [2, 5, 8], [3, 6, 9]))


def task43(**kwargs):
    """
    Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента,
    а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
    :param kwargs:
    :return:
    """
    zoo = dict()
    for k, v in kwargs.items():
        if isinstance(v, (list, dict, set, bytearray)):
            v = str(v)
        zoo[v] = k
    return zoo


# print(task43(dog={'Barbos', 'Tobik'}, cat={'Murka', 'Shurka'}, turtle=['Leonardo', 'Donatello', 'Raphael','Michelangelo'],
#                      parrot={'Petya', 'Vasya', 'Artemka'}))


def task44():
    """
    Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
    Дополнительно сохраняйте все операции поступления и снятия средств в список.
    :return:
    """
    bank = tn.Bank()
    print(bank.start(mode='in', cash=4000000))
    print(bank.start(mode='in', cash=100000))
    print(bank.start(mode='out', cash=100000))
    print(bank.start(mode='in', cash=100000))
    print(bank.start(mode='in', cash=1000000))
    print(bank.start(mode='in', cash=2000000))
    print(bank.start(mode='out', cash=5000000))
    print(bank.start(mode='show'))


# task44()