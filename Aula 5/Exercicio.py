class X:
    def __init__(self, dimensao):
        self.lista = [0] * dimensao

    def j(self, c1, c2):
        self.lista[c1 - 1] = c2

    def h(self, outro_vetor):
        resultado = 0
        for i in range(len(self.lista)):
            resultado += self.lista[i] * outro_vetor.lista[i]
        return resultado
    
    def __repr__(self):
        return f''' {self.lista} '''

x1 = X(5)
x2 = X(5)

print(x1)
print(x2)

for c in range(1, 6):
    x1.j(c, c)
    x2.j(c, 2)

print(x1)
print(x2)
print(x1.h(x2))

x3 = X(3)
x4 = X(3)

print(x3)
print(x4)

for c in range(1, 4):
    x3.j(c, c-2)
    x4.j(c, 10)

print(x3)
print(x4)
print(x3.h(x4))

from random import seed
from random import randint

seed(2284)

def get_random_vector(dimension):
    vector = X(dimension)
    for c in range(1, dimension+1):
        vector.j(c, randint(-2000, 2000))
    return vector

g1 = []
g2 = []
g3 = []

for c in range(423):
    dimension = randint(100, 500)
    x1 = get_random_vector(dimension)
    x2 = get_random_vector(dimension)
    g1.append(x1)
    g2.append(x2)

for i in range(len(g1)):
    g3.append(g1[i].h(g2[i]))

print('só para verificação da geração de números pseudoaleatórios')
x1 = get_random_vector(10)
x2 = get_random_vector(10)
print(x1)
print(x2)
print(x1.h(x2))

print('-------------------------')

print(1.1)
print(g3[0])#true
print(1.2)
print(sum(g3))#false
print(1.3)
print(g3[422])#true
print(1.4)
print(g3[72])#true
print(1.5)
print(g3[361])#true