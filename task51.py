import os


def file_info(file_path):
    """
    Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
    Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
    :param file_path:
    :return:
    """
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension

file_path = "Enter the file path"
print(file_info(file_path))
