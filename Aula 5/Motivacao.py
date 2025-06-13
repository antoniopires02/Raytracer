class Vector3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def dot(self, outro_vetor):
        resultado = self.x * outro_vetor.x
        resultado += self.y * outro_vetor.y
        resultado += self.z * outro_vetor.z

        return resultado