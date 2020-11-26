from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    def desc_conta(self):
        print(f"Agencia: {self.agencia}"
              f"Numero da conta: {self.numero_conta}"
              f"Saldo: {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor

    @abstractmethod
    def sacar(self):
        pass

class ContaCorrente(Conta):
    def sacar(self, valor):
        self.saldo -= valor 
        return valor

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

        else:
            return f"Seu saldo é de {self.saldo}, não é possivel sacar"