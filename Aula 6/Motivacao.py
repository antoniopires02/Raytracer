class Matrix3x3:
    def __init__(self):
        self.linhas = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]    
        
    def __repr__(self):
        resultado = ''
        for i_linha in range(3):
            resultado = resultado + str(self.linhas[i_linha]) + '\n'
        return resultado
    
    def set_entrada(self, n_linha, n_coluna, valor):
        #conversão para índices
        i_linha = n_linha - 1
        i_coluna = n_coluna -1
        
        self.linhas[i_linha][i_coluna] = valor 
        
    def get_entrada(self, n_linha, n_coluna):
        #conversão para índices
        i_linha = n_linha - 1
        i_coluna = n_coluna -1
        
        valor = self.linhas[i_linha][i_coluna]
        
        return valor
    
    def get_linha(self, n_linha):
        #conversão para índices
        i_linha = n_linha - 1
        
        resultado = []
        
        for i_coluna in range(3):
            valor = self.linhas[i_linha][i_coluna]
            resultado.append(valor)
            return resultado
        
    def get_coluna(self, n_coluna):
        #conversão para índices
        i_coluna = n_coluna - 1
        
        resultado = []
        
        for i_linha in range(3):
            valor = self.linhas[i_linha][i_coluna]
            resultado.append(valor)
            return resultado
        