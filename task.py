import csv
from statistics import mean


class NameCheck:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self._check_name(value)
        setattr(obj, self.private_name, value)

    def _check_name(self, value):
        if not isinstance(value, str):
            raise AttributeError('Имя должно быть строковым значением')
        if not value.isalpha():
            raise AttributeError('Имя должно состоять из букв')
        if not value.istitle():
            raise AttributeError('Имя должно начинаться с заглавной буквы')


class ItemCheck:

    def __init__(self, min_value: int = None, max_value: int = None):
        self._min_value = min_value
        self._max_value = max_value

    def __set_name__(self, owner, name):
        self.private_item = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_item)

    def __set__(self, obj, value: dict):
        self._check_range(value)
        self._check_items(value)

        setattr(obj, self.private_item, value)

    def _check_range(self, value: dict):
        for value in value.values():
            for value_tuple in value:
                if not isinstance(value_tuple, int):
                    raise TypeError(f'Значение {value_tuple} должно быть целым числом')
                if value_tuple is not None and value_tuple < self._min_value:
                    raise ValueError(f'Значение {value_tuple} должно быть от {self._min_value}')
                if value_tuple is not None and value_tuple > self._max_value:
                    raise ValueError(f'Значение {value_tuple} должно быть до {self._max_value}')

    def _check_items(self, value: dict):
        data = self._load_data()
        valid = 0
        for d in data:
            for v in value:
                if d == v:
                    valid += 1
        if valid != len(value):
            raise AttributeError(f'Такого предмета нет в списке')

    def _load_data(self):
        data = {}
        file_name = 'lesson.csv'
        i = 0
        with open(file_name, encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            for item in csv_reader:
                res = ''.join(item).strip()
                i += 1
                if i != 1:
                    data[res] = None
        return data


class Student:
    first_name: str = NameCheck()
    last_name: str = NameCheck()
    exams: dict = ItemCheck(2, 5)
    tests: dict = ItemCheck(0, 100)

    def __init__(self):
        self._first_name: str = ''
        self._last_name: str = ''
        self._exams: dict[str: tuple] = {}
        self._tests: dict[str: tuple] = {}

    def __str__(self):
        exams = '\n'.join(f'{k}: {v}' for k, v in self._exams.items())
        tests = '\n'.join(f'{k}: {v}' for k, v in self._tests.items())
        avg_test_results = '\n'.join(f'{k}: {v}' for k, v in self._avg_tests().items())
        avg_grades_result = '\n'.join(f'{k}: {v}' for k, v in self._avg_exams().items())
        return f'Студент:\n{self._first_name} {self._last_name}' \
               f'\n\nОценки по предметам:\n{exams}' \
               f'\n\nРезультаты тестов:\n{tests}' \
               f'\n\nСредний результат тестов:\n{avg_test_results}' \
               f'\n\nСредняя оценка по всем предметам:\n{avg_grades_result}'

    def _avg_tests(self):
        avg_results = dict()
        for key, value in self._tests.items():
            avg_results[key] = round(mean(value), 1)
        return avg_results

    def _avg_exams(self):
        avg_result = 0
        for values in self._exams.values():
            avg_result += mean(values)
        return {'Средний балл по предметам': round(avg_result / len(self._exams.values()), 1)}


if __name__ == '__main__':
    student = Student()
    student.first_name = 'Имя'
    student.last_name = 'Фамилия'
    student.exams = {'Предмет1': (3, 4, 3), 'Предмет2': (3, 4, 5), 'Предмет3': (3, 5, 4, 5)}
    student.tests = {'Предмет4': (40, 100), 'Предмет5': (10, 50, 80), 'Предмет6': (10, 50, 80, 25)}
    print(student)
