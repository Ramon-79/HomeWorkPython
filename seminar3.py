# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


def task1():
    my_list = [9, 17, 9, 7, 39, 2, 7, 15, 42, 15, 2]
    res = set()
    for el in my_list:
        counter = my_list.count(el)
        if counter > 1:
            res.add(el)
    print(list(res))


# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии.


def task2():
    file = open('text.txt', encoding='utf-8', mode='r')
    text = file.read()
    dict_counts = {}
    SHOW_LIMIT = 10
    new_sorted_dictionary = {}
    new_text = text.replace(',', ''). \
        replace('.', ''). \
        replace('!', ''). \
        replace('?', ''). \
        replace('"', ''). \
        lower(). \
        strip()
    words_list = new_text.split()
    for word in words_list:
        counter = words_list.count(word)
        dict_counts[word] = counter
    sorted_values = sorted(dict_counts.values())[::-1]
    for i in sorted_values:
        for k in dict_counts.keys():
            if dict_counts[k] == i:
                new_sorted_dictionary[k] = dict_counts[k]
    print(list(new_sorted_dictionary.items())[0: SHOW_LIMIT])


# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.


def task3():
    stuff = {'whistle': 1, 'dishes': 2, 'tent': 10, 'eat': 5, 'shoes': 3}
    capacity = 15
    packaging = []
    for key, value in stuff.items():
        if value <= capacity:
            capacity -= value
            packaging.append(key)
    print(packaging)
