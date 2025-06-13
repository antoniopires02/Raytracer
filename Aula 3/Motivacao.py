class Vetor3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def soma(self, outro_vetor):
        novo_x = self.x + outro_vetor.x
        novo_y = self.y + outro_vetor.y
        novo_z = self.z + outro_vetor.z

        vetor_soma = Vetor3D(novo_x, novo_y, novo_z)
        return vetor_soma
    
    def __add__(self, outro_vetor):
        return self.soma(outro_vetor)
    
    def __repr__(self):
        return f'''
[{self.x}]
[{self.y}]
[{self.z}]'''

v1 = Vetor3D(1, 2, 3)
v2 = Vetor3D(-1, -1, -1)

print(v1)
print(v2)

#v3 = v1.soma(v2)
v3 = v1 + v2

print(v3)
