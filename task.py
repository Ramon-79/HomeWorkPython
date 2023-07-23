class Matrix:
    """
    Класс матрица. Далее описание, инструкция и т.д.
    """

    def __init__(self, list: list[list[int]]):
        """
        Далее описание, инструкция и т.д.
        :param list:
        """
        self.list = list

    def __str__(self):
        """
        Далее описание, инструкция и т.д.
        :return:
        """
        result = ''
        for row in self.list:
            for elem in row:
                result += ''.join(f'{elem}\t')
            result += ''.join('\n')
        return result

    def __eq__(self, other):
        """
        Далее описание, инструкция и т.д.
        """
        return True if self.list == other.list else False

    def __add__(self, other):
        """
        Далее описание, инструкция и т.д.
        :param other:
        :return:
        """
        result = []
        row = []
        for i in range(len(self.list)):
            for j in range(len(self.list[0])):
                row.append(self.list[i][j] + other.list[i][j])
            result.append(row)
            row = []
        return Matrix(result)

    def __mul__(self, other):
        """
        Далее описание, инструкция и т.д.
        :param other:
        :return:
        """
        m = len(self.list)
        n = len(other.list)
        k = len(other.list[0])
        result = [[0 for _ in range(k)] for _ in range(m)]
        for i in range(m):
            for j in range(k):
                result[i][j] = sum(self.list[i][k] * other.list[k][j] for k in range(n))
        return Matrix(result)


if __name__ == '__main__':
    matrix_1 = Matrix([[5, 5], [5, 5]])
    matrix_2 = Matrix([[5, 5], [5, 5]])
    matrix_sum = matrix_1 + matrix_2
    print(matrix_sum)
    matrix_mul = matrix_1 * matrix_2
    print(matrix_mul)
    if matrix_1 == matrix_2:
        print('True')
    else:
        print('False')

    help(Matrix)
