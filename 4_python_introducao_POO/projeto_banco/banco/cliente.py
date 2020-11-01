class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        Pessoa.__init__(self, nome, idade)
        self.conta = conta


if __name__ == "__main__":
    cliente1 = Cliente("Fernando Santos", 18, 1111)
    print(cliente1.nome)
    print(cliente1.idade)
    print(cliente1.conta)
    


