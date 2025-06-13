class T:
    def __init__(self, n_linhas, n_colunas):
        self.linhas = []
        
        for i in range(n_linhas):
            linha = []
            for j in range(n_colunas):
                linha.append(0)
            self.linhas.append(linha)
            
    def __repr__(self):
        resultado = ''
        for i_linha in range(len(self.linhas)):
            resultado = resultado + str(self.linhas[i_linha]) + '\n'
        return resultado
    
    def r(self, n_linha, n_coluna, valor):
        #conversão para índices
        i_linha = n_linha - 1
        i_coluna = n_coluna -1
        
        self.linhas[i_linha][i_coluna] = valor 
        
    def v(self, n_linha, n_coluna):
        #conversão para índices
        i_linha = n_linha - 1
        i_coluna = n_coluna -1
        
        valor = self.linhas[i_linha][i_coluna]
        
        return valor
    
    def h(self, n_linha):
        #conversão para índices
        i_linha = n_linha - 1
        
        resultado = []
        
        for i_coluna in range(len(self.linhas[i_linha])):
            valor = self.linhas[i_linha][i_coluna]
            resultado.append(valor)
        
        return resultado
        
    def p(self, n_coluna):
        #conversão para índices
        i_coluna = n_coluna - 1
        
        resultado = []
        
        for i_linha in range(len(self.linhas)):
            valor = self.linhas[i_linha][i_coluna]
            resultado.append(valor)
        
        return resultado

n_lines = 3
n_columns = 4
t = T(n_lines, n_columns)
print(t)

for e in range(1, n_lines+1):
    for b in range(1, n_columns+1):
        t.r(e, b, (e-1)*n_lines+(b-1))
print(t)
print(t.h(2))
print(t.p(3))
print(t.v(1, 1))
print(t.v(3, 4))

from random import seed
from random import randint

seed(8655)

def get_random_matrix(n_lines, n_columns):
    matrix = T(n_lines, n_columns)
    for e in range(1, n_lines+1):
        for b in range(1, n_columns+1):
            matrix.r(e, b, randint(-100, 100))
    return matrix

u_1 = []
u_2 = []
u_3 = []
u_4 = []
u_5 = []

for e in range(958):
    n_lines = randint(10, 20)
    n_columns = randint(10, 20)
    t = get_random_matrix(n_lines, n_columns)
    u_1.append(t)
    line_number = randint(1, n_lines)
    column_number = randint(1, n_columns)
    u_2.append(line_number)
    u_3.append(column_number)
    u_4.append(t.h(line_number))
    u_5.append(t.p(column_number))
    
print('só para verificação da geração de valores pseudoaleatórios')
matrix = get_random_matrix(4, 6)
print(matrix)

# 1.1 A soma do último elemento de todas as linhas na lista u_4, é -3308.
last_element_sum_u_4 = sum(row[-1] for row in u_4)
print("1.1:", last_element_sum_u_4 == -3308)

# 1.2 A soma do último elemento de todas as colunas na lista u_5, é -2869.
last_element_sum_u_5 = sum(column[-1] for column in u_5)
print("1.2:", last_element_sum_u_5 == -2869)

# 1.3 A soma da entrada na linha 1, coluna 1, de todas as matrizes na lista u_1, é 1453.
sum_entry_1_1_u_1 = sum(matrix.v(1, 1) for matrix in u_1)
print("1.3:", sum_entry_1_1_u_1 == 1453)

# 1.4 A soma do primeiro elemento de todas as linhas na lista u_4, é 1387.
first_element_sum_u_4 = sum(row[0] for row in u_4)
print("1.4:", first_element_sum_u_4 == 1387)

# 1.5 A soma do primeiro elemento de todas as colunas na lista u_5, é 2682.
first_element_sum_u_5 = sum(column[0] for column in u_5)
print("1.5:", first_element_sum_u_5 == 2682)