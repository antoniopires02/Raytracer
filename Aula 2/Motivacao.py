class Produto:
    def __init__(self, preco, desconto):
        self.preco = preco
        self.desconto = desconto

    def valor_do_desconto(self):
        return self.preco - self.desconto/100
    
    def valor_a_pagar(self):
        return self.preco - self.valor_do_desconto()
    
class ListaDeCompras:
    def __init__ (self):
        self.lista = []

    def adiciona_produto(self, produto):
        self.lista.append(produto)
        #lista_de_produtos = self.lista
        #lista_de_produtos.append(produto) 

    def valor_do_desconto(self):
        desconto_total = 0
        for produto in self.lista:
            desconto_total = desconto_total + produto.valor_do_desconto()
        return desconto_total
    
    def valor_a_pagar(self):
        valor_total = 0
        for produto in self.lista:
            valor_total = valor_total + produto.valor_a_pagar()
        return valor_total