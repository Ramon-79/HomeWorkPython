import argparse
from support import walk_dir


def parse_ars():
    parser = argparse.ArgumentParser(description="HomeWork15")
    parser.add_argument('-p', metavar='path', type=str, nargs='*', default='.', help='Введите путь до директорию')
    args = parser.parse_args()
    return args.p


def main():
    for place in parse_ars():
        for item in (walk_dir(place)):
            print(repr(item))


if __name__ == '__main__':
    main()
