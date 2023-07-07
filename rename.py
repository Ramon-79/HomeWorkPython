import os
from pathlib import Path


def group_rename(lens, old_ext, new_ext, interval, new_name=''):
    count = 0
    for file in os.listdir():
        if file.endswith(old_ext):
            count += 1
            Path(file).rename(f"{file.split('.')[0][interval[0]:interval[1]]}{new_name}{count:0>{lens}}.{new_ext}")


group_rename(2, 'txt', 'png', [2, 2], "new")
