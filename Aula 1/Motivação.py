class UmaClasse:
    def __init__(self, um_argumento):
        self.um_atributo = um_argumento

    def um_metodo(self):
        return self.um_atributo
    
x = UmaClasse(4)

print(x.um_metodo())