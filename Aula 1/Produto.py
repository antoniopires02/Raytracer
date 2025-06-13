class Produto:
    def __init__(self, preco, desconto):
        self.preco = preco
        self.desconto = desconto

    def valor_do_desconto(self):
        return self.preco - self.desconto/100
    
    def valor_a_pagar(self):
        return self.preco - self.valor_do_desconto

