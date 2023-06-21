import fractions


# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def task1():

    i = int(input("Введите число: "))
    h = (format(i, '#x'))
    print(h)
    print(hex(i))


# Напишите программу, которая принимает две строки вида “a/b”
# - дробь с числителем и знаменателем. Программа должна возвращать сумму и
# произведение дробей. Для проверки своего кода используйте модуль fractions.

def task2():

    number1: int = int(input("Введите числитель первой дроби: "))
    number2: int = int(input("Введите знаменатель первой дроби: "))
    number3: int = int(input("Введите числитель второй дроби: "))
    number4: int = int(input("Введите знаменатель второй дроби: "))

    result1 = (number1 / number2) + (number3 / number4)
    result2 = (number1 / number2) * (number3 / number4)
    print(result1)
    print(result2)
    firstfraction = fractions.Fraction(number1, number2)
    secondfraction = fractions.Fraction(number3, number4)
    result3 = firstfraction + secondfraction
    result4 = firstfraction * secondfraction
    print(result3)
    print(result4)
