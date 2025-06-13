class Matrix:
    def __init__(self, n_lines, n_columns):
        self.n_lines = n_lines
        self.n_columns = n_columns
        self.lines = []
        for r in range(self.n_lines):
            new_line = []
            for z in range(self.n_columns):
                new_line.append(0)
            self.lines.append(new_line)


    def __repr__(self):
        result = ''
        for r in range(self.n_lines):
            for z in range(self.n_columns):
                result = result + str(self.lines[r][z]) + ' '
            result = result + '\n'
        return result

    def set_entry(self, n_line, n_column, value):
        # conversion to indexes
        i_line = n_line - 1
        i_column = n_column - 1
        self.lines[i_line][i_column] = value

    def get_entry(self, n_line, n_column):
        # conversion to indexes
        i_line = n_line - 1
        i_column = n_column - 1
        return self.lines[i_line][i_column]

    def __mul__(self, other_matrix):
        result_n_lines = self.n_lines
        result_n_columns = other_matrix.n_columns
        result = Matrix(result_n_lines, result_n_columns)
        for i_line in range(result_n_lines):
            for i_column in range(result_n_columns):
                total = 0
                for k in range(self.n_columns):
                    line_entry = self.lines[i_line][k]
                    column_entry = other_matrix.lines[k][i_column]
                    total = total + line_entry * column_entry
                result.lines[i_line][i_column] = total
        return result

class P(Matrix):
    def __init__(self):
        n_lines = 2
        n_columns = 2
        super().__init__(n_lines, n_columns)

    def j(self):
        # [a b]
        # [c d]
        # det = ad − bc

        a = self.get_entry(1, 1)
        b = self.get_entry(1, 2)
        c = self.get_entry(2, 1)
        d = self.get_entry(2, 2)

        det = a * d - b * c

        return det

p_1 = P()
print('--- matrix 1')
print(p_1)

p_1.set_entry(1, 1, 10)
p_1.set_entry(1, 2, 20)
p_1.set_entry(2, 1, 30)
p_1.set_entry(2, 2, 40)
print('--- matrix 1')
print(p_1)

print('--- matrix 1 determinant')
det = p_1.j()
print(det)

n_lines = 2
n_columns = 3
p_2 = Matrix(n_lines, n_columns)
print('--- matrix 2')
print(p_2)

for r in range(n_lines):
    for z in range(n_columns):
        p_2.set_entry(r+1, z+1, r+z)
print('--- matrix 2')
print(p_2)

p_3 = p_1 * p_2
print('--- matrix 3')
print(p_3)

from random import seed
from random import randint
seed(3094)

def get_random_matrix(n_lines, n_columns):
    if (n_lines == 2) and (n_columns == 2):
        matrix = P()
    else:
        matrix = Matrix(n_lines, n_columns)

    for r in range(n_lines):
        for z in range(n_columns):
            matrix.set_entry(r+1, z+1, randint(-100, 100))
    return matrix

a_1 = []
a_2 = []
a_3 = []
a_4 = []

for r in range(935):
    n_lines_1 = 2
    n_columns_1 = 2
    n_lines_2 = n_columns_1
    n_columns_2 = randint(3, 5)
    p_1 = get_random_matrix(n_lines_1, n_columns_1)
    p_2 = get_random_matrix(n_lines_2, n_columns_2)
    a_1.append(p_1)
    a_2.append(p_2)

for i in range(len(a_1)):
    a_3.append(a_1[i].j())

for i in range(len(a_1)):
    a_4.append(a_1[i] * a_2[i])

print('só para verificação da geração de valores pseudoaleatórios')
matrix = get_random_matrix(3, 4)
print(matrix)

primeiras = []
for i in range(len(a_4)):
    primeiras.append(a_4[i].get_entry(1, 1))

print('----------------------------------------------------------')
print('1.1')
print(a_3[0] == 736)
print('1.2')
print(a_3[748] == 6656)
print('1.3')
print(sum(a_3) == -75361)
print('1.4')
print(sum(primeiras) == -24552)
print('1.5')
print(a_3[-1] == 9124)

