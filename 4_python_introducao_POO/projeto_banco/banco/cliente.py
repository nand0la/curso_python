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

    @property
    def banco(self):
        return self._banco 



class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        Pessoa.__init__(self, nome, idade)
        self._conta = conta

    @property
    def conta(self):
        return self._conta


