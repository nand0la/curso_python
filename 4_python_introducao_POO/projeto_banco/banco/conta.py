from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    
    def depositar(self, valor):
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass 

class ContaCorrente(Conta):
    def sacar(self, valor):
        self.saldo -= valor
        return valor

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return valor
        else:
            print("valor maior que o limite")


if __name__ == "__main__":
    pass  

