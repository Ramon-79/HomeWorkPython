import csv
import json
from pathlib import Path


def task2(file_in, file_out):
    json_list = []
    with open(file_in, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            json_dict = {}
            level, user_id, name = row
            json_dict['level'] = int(level)
            json_dict['id'] = user_id.zfill(3)
            json_dict['name'] = name.title()
            json_list.append(json_dict)

    with open(file_out, 'w', encoding='utf-8') as f:
        json.dump(json_list, f, indent=2)


if __name__ == '__main__':
    task2(Path('file.csv'), Path('file_json.json'))
