def fibonachi(n):
    """
    Создайте функцию генератор чисел Фибоначчи.
    :param n:
    :return:
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(*(fibonachi(10)))
