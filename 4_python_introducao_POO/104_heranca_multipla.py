from mixinClass import LogMixin


class Eletronico:
    def __init__(self, nome):
        self.nome = nome
        self.ligado = False

    def ligar(self):
        if self.ligado:
            print(f"{self.nome} já está ligado")
            return

        self.ligado = True
        print(f"{self.nome} esta ligado")

    def desligar(self):
        if not self.ligado:
            print(f"{self.nome} já esta desligado")
            return

        self.ligado = False
        print(f"{self.nome} esta desligad")


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        Eletronico.__init__(self, nome)
        self.conectado = False

    def conecta(self):
        if self.conectado:
            msg = f"{self.nome} já esta conectado"
            print(msg)
            self.log_erro("dando errado")
            return

        self.conectado = True
        print(f"{self.nome} esta conectado")

    def desconecta(self):
        if not self.conectado:
            print(f"{self.nome} já esta desconectado")
            return

        self.conectado = False
        print(f"{self.nome} esta desconectado")


xiaomi = Smartphone("xiaomi pocofone")
xiaomi.conecta()
xiaomi.conecta()
