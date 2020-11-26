class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    # getter nome
    @property
    def nome(self):
        return self._nome

    # getter idade
    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None

    def inserir_conta(self, conta):
        self.conta = conta

    def informacao_geral(self):
        print(f"nome: {self.nome}"
              f"idade: {self.idade}"
              f"conta: {self.conta}")