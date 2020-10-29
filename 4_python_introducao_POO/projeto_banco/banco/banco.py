from abs import ABC, abstractmethod

class Conta:
    def __init__(self, agencia, num_conta, saldo):
        self._agencia = agencia
        self._num_conta = num_conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia



class ContaCorrente(Conta):
    pass


class ContaPoupanca(Conta):
    pass  