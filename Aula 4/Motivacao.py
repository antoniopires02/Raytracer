class Matrix2x2:
    def __init__(self, m11, m12, m21, m22):
        self.m11 = m11
        self.m12 = m12
        self.m21 = m21
        self.m22 = m22

    def __repr__(self):
        return f'''[{self.m11} {self.m12}]
                   [{self.m21} {self.m22}]'''
    
    def __mul__(self, outra_matriz):
        #[a b] * [e f] = [ae+bg  af+bh]
        #[c d] * [g h] = [ce+dg  cf+dh]

        a = self.m11
        b = self.m12
        c = self.m21
        d = self.m22

        e = outra_matriz.m11
        f = outra_matriz.m12
        g = outra_matriz.m21
        h = outra_matriz.m22

        m11_produto = a*e+b*g
        m12_produto = a*f+b*h
        m21_produto = c*e+d*g
        m22_produto = c*f+d*h

        #nova matriz
        produto = Matrix2x2(m11_produto, m12_produto, m21_produto, m22_produto)
        return produto
    
    def tr(self):
        return self.m11 + self.m22




