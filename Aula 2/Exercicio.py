class S:
    def __init__(self, km, combustivel):
        self.e = km
        self.d = combustivel

    def f(self):
        return self.d/self.e * 100 
    
class Y:
    def __init__(self):
        self.lista = []

    def u(self, carro):
        self.lista.append(carro)

    def d(self):
        combustivel_gasto = 0
        for carro in self.lista:
            combustivel_gasto = combustivel_gasto + carro.d
        return combustivel_gasto
    
    def e(self):
        km_percorridos = 0
        for carro in self.lista:
            km_percorridos = km_percorridos + carro.e
        return km_percorridos
    
    def f(self):
        consumo_frota = 0
        consumo_frota = self.d()/ self.e() * 100
        return consumo_frota 


s_1 = S(200, 20)
print(round(s_1.f()))
print(s_1.e)
print(s_1.d)
s_2 = S(400, 40)
s_3 = S(800, 80)
s_4 = S(100, 10)
s_5 = S(200, 50)

y_1 = Y()
y_1.u(s_1)
y_1.u(s_2)
y_1.u(s_3)
y_2 = Y()
y_2.u(s_4)
y_2.u(s_5)

print('*****')
print(y_1.d())
print(y_1.e())
print(round(y_1.f()))
print('*****')
print(y_2.d())
print(y_2.e())
print(round(y_2.f()))

from random import seed
from random import randint

seed(9240)

p = []
for v in range(1081):
    y = Y()
    for q in range(72):
        h = randint(100, 1081)
        x = randint(10, 900)
        s = S(h, x)
        y.u(s)
    p.append(y)

print('só para verificação da geração de números pseudoaleatórios')
print(p[0].d())
print(p[0].e())
print(round(p[0].f()))
print(p[1081-1].d())
print(p[1081-1].e())
print(round(p[1081-1].f()))

print('-------------------------')

print('1.1')
print(p[384].lista[0].e)#true

print('1.2')
print(round(p[961].f()))

print('1.3')
print(p[584].lista[-1].d)

print('1.4')
print(round(p[322].f()))

print('1.5')
print(round(p[500].f()))