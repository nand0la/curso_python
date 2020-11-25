from abc import ABC, abstractmethod

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
        print(f"nome: {self.nome} \nidade: {self.idade} \nconta: {self.conta}")


##############################################################################

class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

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
            print(f"Seu saldo é de {self.saldo} não pode sacar mais que isso")


##############################################################################