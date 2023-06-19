import seminar2


print("Задача 21:  Перевод целого числа в шестнадцатеричное")
print("Задача 22:  Cуммa и произведение дробей")

print("Enter 0 for EXIT!!!")

while (True):
    n = input("Enter number task: ")

    match n:

        case '0':
            print("See you soon")
            break
        case '21':
            seminar2.task1()
        case '22':
            seminar2.task2()
        case _:
            print("Такой задачи нет, повторите попытку")
            continue
