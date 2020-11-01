"""
    getter - obtem um valor baseado em uma condição
    setter - seta um valor baseado em uma condicao
"""


class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self.preco = preco

    # getter -> nome da funcao tem que ter o nome do que precisa ser retornado
    @property
    def nome(self):
        return self._nome

    # setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()


p1 = Produto("CELULAR", 14512)
print(p1.nome)
