class ExcecaoMatrizNaoInvertivel(Exception):
    pass

class U:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __repr__(self):
        return f'{self.a} {self.b}\n{self.c} {self.d}'

    def b(self):
        det = self.a * self.d - self.b * self.c
        if det == 0:
            raise ExcecaoMatrizNaoInvertivel("A matriz não é invertível.")
        inv_a = self.d / det
        inv_b = -self.b / det
        inv_c = -self.c / det
        inv_d = self.a / det
        return U(inv_a, inv_b, inv_c, inv_d)

    def get_value(self, row, col):
        if row == 1 and col == 1:
            return self.a
        elif row == 1 and col == 2:
            return self.b
        elif row == 2 and col == 1:
            return self.c
        elif row == 2 and col == 2:
            return self.d
        else:
            raise IndexError("Index out of range for 2x2 matrix")

from random import seed, randint, choice

seed(4168)

def get_random_matrix():
    a = randint(-100, 100)
    b = randint(-100, 100)
    c = randint(-100, 100)
    d = randint(-100, 100)
    matrix = U(a, b, c, d)
    if choice([True, False]):
        b = a
        d = c
        matrix = U(a, b, c, d)
    return matrix

k_1 = []
k_2 = []

for _ in range(1037):
    u_1 = get_random_matrix()
    k_1.append(u_1)
    try:
        inv_u_1 = u_1.b()
        k_2.append(inv_u_1)
    except ExcecaoMatrizNaoInvertivel:
        continue

sum_2_1 = round(sum(matrix.get_value(2, 1) for matrix in k_2))
sum_2_2 = round(sum(matrix.get_value(2, 2) for matrix in k_2))
sum_1_2 = round(sum(matrix.get_value(1, 2) for matrix in k_2))
num_invertible = len(k_2)
sum_1_1 = round(sum(matrix.get_value(1, 1) for matrix in k_2))

print(f"A soma da entrada na linha 2, coluna 1, de todas as matrizes na lista k_2, arredondada para um número inteiro usando a função built-in round, é {sum_2_1}.")
print(f"A soma da entrada na linha 2, coluna 2, de todas as matrizes na lista k_2, arredondada para um número inteiro usando a função built-in round, é {sum_2_2}.")
print(f"A soma da entrada na linha 1, coluna 2, de todas as matrizes na lista k_2, arredondada para um número inteiro usando a função built-in round, é {sum_1_2}.")
print(f"Existem {num_invertible} matrizes invertíveis na lista k_1.")
print(f"A soma da entrada na linha 1, coluna 1, de todas as matrizes na lista k_2, arredondada para um número inteiro usando a função built-in round, é {sum_1_1}.")

# Verificação das afirmações
print(f"1.1: {sum_2_1 == -14}")
print(f"1.2: {sum_2_2 == -18}")
print(f"1.3: {sum_1_2 == -4}")
print(f"1.4: {num_invertible == 507}")
print(f"1.5: {sum_1_1 == -19}")
