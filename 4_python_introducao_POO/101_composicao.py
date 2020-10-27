"""
    classe dona de outro objeto
    se a classe principal for apagada
    os outros objetos agregados a ela tambem serão
"""


class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def listar_endereco(self):
        for v in self.enderecos:
            print(v.cidade, v.estado)


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado


c1 = Cliente("Fernando", 19)
c1.insere_endereco("Rio de Janeiro", "RJ")
c1.insere_endereco("São Paulo", "SP")
c1.listar_endereco()
