class ExcecaoVetorNulo(Exception):
    'Exceção lançada quando se tenta obter o versor do vetor nulo'


class Vetor2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str(self.x) + '\n' + str(self.y)

    def __add__(self, v):
        soma_x = (self.x + v.x)
        soma_y = (self.y + v.y)

        soma_vetor = Vetor2D(soma_x, soma_y)

        return soma_vetor

    def versor(self):

        try:
            x = self.x
            y = self.y

            versor_x = x / ((x**2 + y**2)**(0.5))
            versor_y = y / ((x ** 2 + y ** 2) ** (0.5))
            versor_vetor = Vetor2D(versor_x, versor_y)

            return versor_vetor

        except ZeroDivisionError:
            raise ExcecaoVetorNulo