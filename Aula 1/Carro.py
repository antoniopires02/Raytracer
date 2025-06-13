class V:
    def __init__(self, km, combustivel):
        self.c = km
        self.y = combustivel

    def k(self):
        return self.c
    
    def c(self):
        return self.y

    def a(self):
        return self.y/self.c * 100 
    
v_1 = V(400, 20)
print(round(v_1.a()))
print(v_1.c)
print(v_1.y)

v_2 = V(956, 100)
print(round(v_2.a()))
print(v_2.c)
print(v_2.y)

from random import seed
from random import randint

seed(2230)

d = []
for r in range(956):
    e = randint(100, 900)
    w = randint(10, 90)
    v = V(e, w)
    d.append(v)


print('----------------')

print('1.1')
print(round(d[340].a()))
print('1.2')
print(round(d[955].a()))
print('1.3')
print(round(d[650].a()))
print('1.4')
print(d[567].c)
print('1.5')
print(d[305].y)