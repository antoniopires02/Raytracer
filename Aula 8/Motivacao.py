class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'''[{self.x}]
                   [{self.y}]'''

    def produto_interno(self, outro_vector):
        parcela1 = self.x * outro_vector.x
        parcela2 = self.y * outro_vector.y

        return parcela1 + parcela2

    def produto_escalar(self, numero):
        novo_x = self.x * numero
        novo_y = self.y * numero
        novo_vector = Vector2D(novo_x, novo_y)

        return novo_vector

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return self.produto_interno(other)
        else:
            return self.produto_escalar(other)