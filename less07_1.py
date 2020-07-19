class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        result = ''
        max_len = 0
        for i in self.lists:
            for j in i:
                if len(str(j)) > max_len:
                    max_len = len(str(j))
        for li in self.lists:
            for i, el in enumerate(li):
                result += str(el) + ' ' * (max_len - len(str(el))) + ' '
            if i == len(li) - 1:
                result += '\n'
        return result

    def __add__(self, other):
        e = []
        for i in self.lists:
            result = []
            for ind, j in enumerate(i):
                for el in other.lists:
                    for indx, j2 in enumerate(el):
                        if self.lists.index(i) == other.lists.index(el) and ind == indx:
                            result.append(j + j2)
            e.append(result)
        return Matrix(e)


matrix = Matrix([[1, 22, 3], [278, 3, 4], [6, 12, 4], [120, 2, 3]])
matrix_2 = Matrix([[1, 8, 3], [32, 3, 4], [18, 3, 4], [1, 2, 3]])
print(f'Matrix 1 is:\n{matrix}')
print(f'Matrix 2 is:\n{matrix_2}')
new_matrix = matrix + matrix_2
print(f'The sum of two matrix is:\n{new_matrix}')
