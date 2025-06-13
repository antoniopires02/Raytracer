class G:
    def __init__(self, m11, m12, m21, m22, m31, m32):
        self.m11 = m11
        self.m12 = m12
        self.m21 = m21
        self.m22 = m22
        self.m31 = m31
        self.m32 = m32

    def __add__(self, outro_vetor):
        novo_m11 = self.m11 + outro_vetor.m11
        novo_m12 = self.m12 + outro_vetor.m12
        novo_m21 = self.m21 + outro_vetor.m21
        novo_m22 = self.m22 + outro_vetor.m22
        novo_m31 = self.m31 + outro_vetor.m31
        novo_m32 = self.m32 + outro_vetor.m32

        resultado = G(novo_m11, novo_m12, novo_m21, novo_m22, novo_m31, novo_m32)
        return resultado
    
    def __repr__(self):
        return f'''
                [{self.m11} {self.m12}]
                [{self.m21} {self.m22}]
                [{self.m31} {self.m32}]
                '''

g_1 = G(1, 2, 3, 4, 5, 6)
g_2 = G(1, 1, 2, 2, 3, 3)
g_3 = g_1 + g_2
print(g_1)
print('-----')
print(g_2)
print('-----')
print(g_3)

from random import seed
from random import randint

seed(5795)

def get_random_matrix():
    n = randint(-100, 100)
    x = randint(-100, 100)
    i = randint(-100, 100)
    k = randint(-100, 100)
    e = randint(-100, 100)
    p = randint(-100, 100)
    a_matrix = G(n, x, i, k, e, p)
    return a_matrix

b_1 = []
b_2 = []
b_3 = []

for c in range(972):
    b_1.append(get_random_matrix())
    b_2.append(get_random_matrix())

soma = 0

for i in range(len(b_1)):
    b_3.append(b_1[i] + b_2[i])

print('só para verificação da geração de números pseudoaleatórios')
print(b_2[972-3])
print('-----')
print(b_2[972-2])
print('-----')
print(b_2[972-1])


print('1')
print(b_3[600].m31)#true

print('2')
print(b_3[734].m31)#false

print('3')
print(b_3[859].m32)#false

print('4')
print(b_3[905].m12)#false

print('5')
print(b_3[794].m32)#true