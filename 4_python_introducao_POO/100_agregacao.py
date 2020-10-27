"""
    classes necessita da outra
"""


class Carrinho:
    def __init__(self):
        self.produtos = []

    def insert_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        return sum([produto.valor for produto in self.produtos])


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


carrinho = Carrinho()
p1 = Produto("Colher de Pau", 7.5)
p2 = Produto("Camisa", 25)
p3 = Produto("Caneca", 13)

carrinho.insert_produto(p1)
carrinho.insert_produto(p2)
carrinho.insert_produto(p3)

carrinho.listar_produtos()
total_compra = carrinho.soma_total()
print(total_compra)
