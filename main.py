import seminar4


print("Задача 41:  Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s")
print("Задача 42:  Напишите функцию для транспонирования матрицы")
print("Задача 43:  Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь")
print("Задача 44:  Возьмите задачу из семинара 2. Разбейте её на отдельные операции — функции")

print("Enter 0 for EXIT!!!")

while (True):
    n = input("Enter number task: ")

    match n:

        case '0':
            print("See you soon")
            break
        case '41':
            seminar4.task41('sos', 'heh', 'соs', 's')
        case '42':
            print(seminar4.task42([1, 4, 7], [2, 5, 8], [3, 6, 9]))
        case '43':
            print(seminar4.task43(dog={'Barbos', 'Tobik'}, cat={'Murka', 'Shurka'}, turtle=['Leonardo', 'Donatello', 'Raphael', 'Michelangelo'],
                            parrot={'Petya', 'Vasya', 'Artemka'}))
        case '44':
            seminar4.task44()
        case _:
            print("Такой задачи нет, повторите попытку")
            continue
