import seminar3


print("Задача 31:  Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами")
print("Задача 32:  В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых")
print("Задача 33:  Создайте словарь со списком вещей для похода в качестве ключа")

print("Enter 0 for EXIT!!!")

while (True):
    n = input("Enter number task: ")

    match n:

        case '0':
            print("See you soon")
            break
        case '31':
            seminar3.task1()
        case '32':
            seminar3.task2()
        case '33':
            seminar3.task3()
        case _:
            print("Такой задачи нет, повторите попытку")
            continue
