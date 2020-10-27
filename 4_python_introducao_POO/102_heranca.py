class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):
    def comprar(self):
        print(f"{self.nome} esta comprando")


class ClienteVIP(Cliente):
    def __init__(self, nome, idade):
        Pessoa.__init__(self, nome, idade)


class Aluno(Pessoa):
    def estudar(self):
        print(f"{self.nome} esta estudando")


alunos1 = Aluno("Fernando", 16)
alunos1.estudar()
