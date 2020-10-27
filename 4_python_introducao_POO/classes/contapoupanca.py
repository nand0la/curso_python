from classes.conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print("saldo insuficiene")
            return

        self.saldo -= valor

