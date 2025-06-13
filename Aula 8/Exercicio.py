class I:
    def __init__(self, m11, m12, m21, m22):
        self.m11 = m11
        self.m12 = m12
        self.m21 = m21
        self.m22 = m22

    def __repr__(self):
        return f'''
        [{self.m11} {self.m12}]
        [{self.m21} {self.m22}]'''

    def z(self, outra_matriz):
        parcela11 = self.m11 * outra_matriz.m11 + self.m12 * outra_matriz.m21
        parcela12 = self.m11 * outra_matriz.m12 + self.m12 * outra_matriz.m22
        parcela21 = self.m21 * outra_matriz.m11 + self.m22 * outra_matriz.m21
        parcela22 = self.m21 * outra_matriz.m12 + self.m22 * outra_matriz.m22

        return I(parcela11, parcela12, parcela21, parcela22)

    def y(self, numero):
        novo_m11 = self.m11 * numero
        novo_m12 = self.m12 * numero
        novo_m21 = self.m21 * numero
        novo_m22 = self.m22 * numero
        nova_matriz = I(novo_m11, novo_m12, novo_m21, novo_m22)

        return nova_matriz

    def __mul__(self, other):
        if isinstance(other, I):
            return self.z(other)
        else:
            return self.y(other)



i_1 = I(1, 2, 3, 4)
i_2 = I(5, 6, 7, 8)
r = 3
i_3 = i_1.z(i_2)
i_4 = i_1.y(r)
i_5 = i_1 * i_2
i_6 = i_1 * r
print(i_1)
print(i_2)
print(i_3)
print(i_4)
print(i_5)
print(i_6)

from random import seed
from random import randint
from random import choice

seed(8678)

def c():
    d = randint(-100, 100)
    a = randint(-100, 100)
    e = randint(-100, 100)
    h = randint(-100, 100)
    i_1 = I(d, a, e, h)
    return i_1

def n():
    if choice([True, False]) == True:
        return c()
    else:
        return randint(-100, 100)

b_1 = []
b_2 = []

for v in range(1027):
    i_1 = c()
    a_value = n()
    b_1.append(i_1)
    b_2.append(a_value)

print('só para verificação da geração de números pseudoaleatórios')
print(b_1[0])
print(b_1[1])
print(b_2[0])
print(b_2[1])

# Create b_3
b_3 = [i1 * i2 if isinstance(i2, I) else i1 * i2 for i1, i2 in zip(b_1, b_2)]

# Define functions to check statements
def check_statement_1_1():
    sum_21 = sum(matrix.m21 for matrix in b_3)
    return sum_21 == 12321

def check_statement_1_2():
    sum_22 = sum(matrix.m22 for matrix in b_3)
    return sum_22 == -132445

def check_statement_1_3():
    total_sum = sum(matrix.m11 + matrix.m12 + matrix.m21 + matrix.m22 for matrix in b_3)
    return total_sum == 283693

def check_statement_1_4():
    sum_11 = sum(matrix.m11 for matrix in b_3)
    return sum_11 == 161808

def check_statement_1_5():
    sum_12 = sum(matrix.m12 for matrix in b_3)
    return sum_12 == 242002

# Print results
print("Resolução")
print()

# Check and print statements
print("1.1")
print(check_statement_1_1())

print("\n1.2")
print(check_statement_1_2())

print("\n1.3")
print(check_statement_1_3())

print("\n1.4")
print(check_statement_1_4())

print("\n1.5")
print(check_statement_1_5())
