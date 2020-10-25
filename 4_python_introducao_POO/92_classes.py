class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} já esta comendo")
            return

        self.comendo = True
        print(f"{self.nome} está comendo")

    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não esta comendo")

    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} esta comendo")


p1 = Pessoa("Fernando", 15)
p1.comer("comida")
