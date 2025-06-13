class G:
    def __init__(self, n_linhas, n_colunas):
        self.n_linhas = n_linhas
        self.n_colunas = n_colunas

        self.matriz = []
        for i in range(self.n_linhas):
            linha = []
            for j in range(self.n_colunas):
                linha.append(0)
            self.matriz.append(linha)

    def __repr__(self):
        resultado = ''
        for linha in self.matriz:
            resultado += str(linha) + '\n'
        return resultado

    def b(self, n_linha, n_coluna, valor):
        # conversão para índices
        i_linha = n_linha - 1
        i_coluna = n_coluna - 1

        self.matriz[i_linha][i_coluna] = valor

    def u(self, n_linha, n_coluna):
        # conversão para índices
        i_linha = n_linha - 1
        i_coluna = n_coluna - 1

        valor = self.matriz[i_linha][i_coluna]

        return valor

    def __mul__(self, outra_matriz):
        # criar matriz com dimensões de multiplicação
        resultado = G(self.n_linhas, outra_matriz.n_colunas)

        # percorrer linhas
        for il in range(resultado.n_linhas):
            # percorrer colunas
            for ic in range(resultado.n_colunas):
                total = 0
                for k in range(self.n_colunas):
                    total += self.matriz[il][k] * outra_matriz.matriz[k][ic]
                resultado.matriz[il][ic] = total

        return resultado

n_lines   = 2
n_columns = 3
g_1 = G(n_lines, n_columns)
print(g_1)

for r in range(1, n_lines+1):
    for q in range(1, n_columns+1):
        g_1.b(r, q, (r-1)*n_lines+(q-1))

print('---')
print(g_1)
print(g_1.u(1, 1))
print(g_1.u(1, 2))
print(g_1.u(1, 3))
print(g_1.u(2, 1))
print(g_1.u(2, 2))
print(g_1.u(2, 3))

n_lines = 3
n_columns = 4
g_2 = G(n_lines, n_columns)
for r in range(1, n_lines+1):
    for q in range(1, n_columns+1):
        g_2.b(r, q, 6+(r-1)*n_lines+(q-1))

print('---')
print(g_2)
g_3 = g_1 * g_2

print('---')
print(g_3)

from random import seed
from random import randint
seed(8736)

def get_random_matrix(n_lines, n_columns):
    matrix = G(n_lines, n_columns)
    for r in range(1, n_lines+1):
        for q in range(1, n_columns+1):
            matrix.b(r, q, randint(-100, 100))
    return matrix

h_1 = []
h_2 = []
h_3 = []  # Lista para armazenar os produtos de h_1 e h_2

for r in range(1054):
    n_lines_1 = randint(5, 10)
    n_columns_1 = randint(5, 10)
    n_lines_2 = n_columns_1
    n_columns_2 = randint(5, 10)
    g_1 = get_random_matrix(n_lines_1, n_columns_1)
    g_2 = get_random_matrix(n_lines_2, n_columns_2)
    h_1.append(g_1)
    h_2.append(g_2)

# Calculando h_3
for i in range(len(h_1)):
    h_3.append(h_1[i] * h_2[i])


print('só para verificação da geração de valores pseudoaleatórios')
matrix = get_random_matrix(4, 6)
print(matrix)

# Somas solicitadas
sum_1_1 = 0
sum_1_2 = 0
sum_1_3 = 0
sum_1_4 = 0
sum_1_5 = 0

for matrix in h_3:
    # Soma da entrada na linha 5, coluna 5
    sum_1_1 += matrix.u(5, 5)

    # Soma da entrada na linha 1, coluna 2
    sum_1_2 += matrix.u(1, 2)

    # Soma da entrada na linha 4, coluna 1
    sum_1_3 += matrix.u(4, 1)

    # Soma da entrada na linha 3, coluna 3
    sum_1_4 += matrix.u(3, 3)

    # Soma da entrada na linha 2, coluna 4
    sum_1_5 += matrix.u(2, 4)

# Verificação das somas
print("1.1:", sum_1_1 == -114692)
print("1.2:", sum_1_2 == 365839)
print("1.3:", sum_1_3 == -1168)
print("1.4:", sum_1_4 == 75657)
print("1.5:", sum_1_5 == 108707)