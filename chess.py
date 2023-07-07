import random


def make_desk(size):
    EMPTY = 0
    return [[EMPTY for _ in range(size)] for _ in range(size)]


def show_desk(desk: list[[int]]) -> None:
    print()
    print(*desk, sep='\n')



def feel_desk(desk, queens):
    BUSY = 1
    for i in range(len(queens)):
        desk[queens[i][0]][queens[i][1]] = BUSY
    return desk


def _check_turns(desk):
    counter = 0
    for col in desk:
        for el in col:
            if el == 1:
                counter += 1
        if counter > 1:
            return False
        else:
            counter = 0
    return True


def _transparent(desk):
    return [[*col] for col in zip(*desk)]


def _make_all_diagonal(desk):
    n = len(desk)
    all_diags = []
    main, second = _check_main_diagonal(desk)
    all_diags.append(main)
    all_diags.append(second)
    for distance in range(1, n):
        sum_tl = n - 1 - distance
        sum_br = n - 1 + distance
        all_diags.extend([
            [desk[i][sum_tl - i] for i in range(n - distance)],
            [desk[i][sum_br - i] for i in range(distance, n)]
        ])

    return all_diags


def is_beat(size, queens):
    desk = make_desk(size)
    desk_with_queens = feel_desk(desk, queens)
    if _check_turns(desk_with_queens):
        rotate_desk = _transparent(desk_with_queens)
        if _check_turns(rotate_desk):
            diagonal_desk = _make_all_diagonal(desk_with_queens)
            if _check_turns(diagonal_desk):
                return True
    return False


def _check_main_diagonal(desk):
    main_diag = [desk[i][i] for i in range(len(desk))]
    secondary_diagonal = [desk[i][len(desk) - i - 1] for i in range(len(desk))]
    return [main_diag, secondary_diagonal]


def generate_queens_coordinates():
    LENGTH_COORDINATES = 8
    coordinates = []
    i = 0
    while i <= LENGTH_COORDINATES - 1:
        x, y = random.randint(0, 7), random.randint(0, 7)
        if (x, y) not in coordinates:
            coordinates.append((x, y))
            i += 1
    return coordinates


def show_success():
    SIZE = 8
    count = 4
    while count > 0:
        coord_queens = generate_queens_coordinates()
        result = is_beat(SIZE, coord_queens)
        if result:
            desk_with_queens = feel_desk(make_desk(SIZE), coord_queens)
            show_desk(desk_with_queens)
            print(result)
            count -= 1


if __name__ == "__main__":
    desk_1 = make_desk(8)
    desk_2 = make_desk(8)
    queens = [(0, 0), (1, 1), (0, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]
    desk_with_queens_1 = feel_desk(desk_1, queens)
    show_desk(desk_with_queens_1)
    print(is_beat(8, queens))
    print()
    queens_2 = [(0, 3), (1, 1), (2, 7), (3, 4), (4, 6), (5, 0), (6, 2), (7, 5)]
    desk_with_queens_2 = feel_desk(desk_2, queens_2)
    show_desk(desk_with_queens_2)
    print(is_beat(8, queens_2))
    show_success()