import csv
import json
from cmath import sqrt
import random
from typing import Callable


def find_in_csv(func: Callable) -> object:
    def wrapper(*args, **kwargs):
        equations = {}
        with open('random.csv', 'r') as f:
            reader = csv.reader(f, dialect='excel')
            count = 0
            equation = {}
            for row in reader:
                if count > 0:
                    equation = {count: {'a': int(row[0]),
                                        'b': int(row[1]),
                                        'c': int(row[2]),
                                        'result': func(int(row[0]), int(row[1]), int(row[2]))}}
                equations.update(equation)
                count += 1
        return equations

    return wrapper


def write_json(func: Callable):
    def wrapper(*args, **kwargs):
        result = func()
        # print(result)
        with open('result.json', 'w', newline='', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

    return wrapper


@write_json
@find_in_csv
def find_quadratic(a: int = 1, b: int = 1, c: int = 1) -> tuple[str, str] | str:
    discriminant = (pow(b, 2)) - (4 * a * c)
    if discriminant < 0:
        return f'нет корней'
    if discriminant == 0:
        return str(-b / (2 * a))
    else:
        if a != 0:
            return str((-b + sqrt(discriminant)) / (2 * a)), str((-b - sqrt(discriminant)) / (2 * a))


def gen_csv(name: str = 'random', rows_count: int = 150, min_num: int = -999, max_num: int = 1000):
    rows = []
    for _ in range(rows_count):
        a, b, c = random.sample(range(min_num, max_num), 3)
        rows.append({'a': a, 'b': b, 'c': c})
    with open(name + '.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['a', 'b', 'c']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)





if __name__ == '__main__':
    gen_csv()
    find_quadratic()
