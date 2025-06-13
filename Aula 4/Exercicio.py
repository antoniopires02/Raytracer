class M:
    def __init__(self, m11, m12, m13, m21, m22, m23, m31, m32, m33):
        self.m11 = m11
        self.m12 = m12
        self.m13 = m13
        self.m21 = m21
        self.m22 = m22
        self.m23 = m23
        self.m31 = m31
        self.m32 = m32
        self.m33 = m33

    def __repr__(self):
        return f'''
        [{self.m11} {self.m12} {self.m13}] 
        [{self.m21} {self.m22} {self.m23}]
        [{self.m31} {self.m32} {self.m33}]'''
    
    def __mul__(self, outra_matriz):
        #[a b c] * [j k l] = [aj+bm+cp  ak+bn+cq  al+bo+cr]
        #[d e f] * [m n o] = [dj+em+fp  dk+en+fq  dl+eo+fr]
        #[g h i] * [p q r] = [gj+hm+ip  gk+hn+iq  gl+ho+ir]

        a = self.m11
        b = self.m12
        c = self.m13
        d = self.m21
        e = self.m22
        f = self.m23
        g = self.m31
        h = self.m32
        i = self.m33

        j = outra_matriz.m11
        k = outra_matriz.m12
        l = outra_matriz.m13
        m = outra_matriz.m21
        n = outra_matriz.m22
        o = outra_matriz.m23
        p = outra_matriz.m31
        q = outra_matriz.m32
        r = outra_matriz.m33

        m11_produto = (a*j)+(b*m)+(c*p)
        m12_produto = (a*k)+(b*n)+(c*q)
        m13_produto = (a*l)+(b*o)+(c*r)
        m21_produto = (d*j)+(e*m)+(f*p)
        m22_produto = (d*k)+(e*n)+(f*q)
        m23_produto = (d*l)+(e*o)+(f*r)
        m31_produto = (g*j)+(h*m)+(i*p)
        m32_produto = (g*k)+(h*n)+(i*q)
        m33_produto = (g*l)+(h*o)+(i*r)

        #nova matriz
        produto = M(m11_produto, m12_produto, m13_produto, m21_produto, m22_produto, m23_produto, m31_produto, m32_produto, m33_produto)
        return produto
    
    def p(self):
        return self.m11 + self.m22 + self.m33


m1 = M(1, 2, 3, 4, 5, 6, 7, 8, 9)
m2 = M(-9, -8, -7, -6, -5, -4, -3, -2, -1)
m3 = m1 * m2
print(m1)
print(m2)
print(m3)
print(m1.p())
print(m2.p())
print(m3.p())

from random import seed
from random import randint

seed(4165)

def u():
    e1 = randint(-100, 100)
    e2 = randint(-100, 100)
    e3 = randint(-100, 100)
    e4 = randint(-100, 100)
    e5 = randint(-100, 100)
    e6 = randint(-100, 100)
    e7 = randint(-100, 100)
    e8 = randint(-100, 100)
    e9 = randint(-100, 100)
    m1 = M(e1, e2, e3, e4, e5, e6, e7, e8, e9)
    return m1

r1 = []
r2 = []
r3 = []

for w in range(1097):
    m1 = u()
    m2 = u()
    r1.append(m1)
    r2.append(m2)

for i in range(len(r1)):
    r3.append(r1[i] * r2[i])

print('só para verificação da geração de números pseudoaleatórios')
print(r1[0])
print(r1[1])
print(r2[0])
print(r2[1])

print('----------------------------------')
print(1.1)
print(r2[836].m23)#true
print(1.2)
print(r3[554].p())#false
print(1.3)
print(r3[628].m13)#false
print(1.4)
print(r3[37].p())#true
print(1.5)
print(r3[430].p())#false