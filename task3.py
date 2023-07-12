import csv
import json
import os
import pickle


def get_dir(direct):
    sum_dirs = 0
    dict_dir = {}
    types = ['file', 'folder']
    for i, file in enumerate(os.listdir(direct), 1):
        path = os.path.join(direct, file)
        item_dict = {'name': path.split('\\')[-1], 'parent': path.split('\\')[-2], 'type': None, 'size': None}
        dict_dir[i] = item_dict
        if os.path.isfile(path):
            item_dict['size'] = f'{os.path.getsize(path)} b'
            item_dict['type'] = types[0]
        elif os.path.isdir(path):
            sum_dirs += os.path.getsize(path)
            item_dict['size'] = f'{sum_dirs} b'
            item_dict['type'] = types[1]
            dict_dir.update(get_dir(path))
    return dict_dir


def write_json(file, data):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def write_csv(file, data):
    with open(file, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='excel', quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
        writer.writerow(('id', 'name', 'parent', 'type', 'size'))
        for k, v in data.items():
            writer.writerow((k, v['name'], v['parent'], v['type'], v['size']))


def write_pickle(file, data):
    with open(file, 'wb') as f:
        pickle.dump(data, f)


if __name__ == '__main__':
    dict_json = get_dir('Enter path')
    write_json('info.json', dict_json)
    write_csv('info.csv', dict_json)
    write_pickle('info.pickle', dict_json)
