class Matrix:
    def __init__(self, n_lines, n_columns):
        self.n_lines = n_lines
        self.n_columns = n_columns
        self.lines = []

        for n in range(self.n_lines):
            new_line = []
            for m in range(self.n_columns):
                new_line.append(0)
            self.lines.append(new_line)

    def __repr__(self):
        result = ''
        for n in range(self.n_lines):
            for m in range(self.n_columns):
                result = result + str(self.lines[n][m]) + ' '
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

class Matrix3x3(Matrix):
    def __init__(self):
        n_lines = 3
        n_columns = 3
        super().__init__(n_lines, n_columns)

    def determinant(self):
        # [a b c] a b
        # [d e f] d e
        # [g h i] g h
        # det = aei + bfg + cdh - gec - hfa - idb

        a = self.get_entry(1, 1)
        b = self.get_entry(1, 2)
        c = self.get_entry(1, 3)
        d = self.get_entry(2, 1)
        e = self.get_entry(2, 2)
        f = self.get_entry(2, 3)
        g = self.get_entry(3, 1)
        h = self.get_entry(3, 2)
        i = self.get_entry(3, 3)

        det = a*e*i + b*f*g + c*d*h - g*e*c - h*f*a - i*d*b

        return det

matrix_1 = Matrix3x3()
print('--- matrix 1')
print(matrix_1)

matrix_1.set_entry(1, 1, 1)
matrix_1.set_entry(1, 2, 2)
matrix_1.set_entry(1, 3, 3)
matrix_1.set_entry(2, 1, 4)
matrix_1.set_entry(2, 2, 5)
matrix_1.set_entry(2, 3, 6)
matrix_1.set_entry(3, 1, 7)
matrix_1.set_entry(3, 2, 8)
matrix_1.set_entry(3, 3, 9)
print('--- matrix 1')
print(matrix_1)
print('--- matrix 1 determinant')

det = matrix_1.determinant()
print(det)

n_lines = 3
n_columns = 4
matrix_2 = Matrix(n_lines, n_columns)
print('--- matrix 2')
print(matrix_2)

for n in range(n_lines):
    for m in range(n_columns):
        matrix_2.set_entry(n+1, m+1, n+m)
print('--- matrix 2')
print(matrix_2)
matrix_3 = matrix_1 * matrix_2
print('--- matrix 3')
print(matrix_3)


