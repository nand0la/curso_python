class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        Pessoa.__init__(self, nome, idade)
        self.conta = conta


if __name__ == "__main__":
    pass
