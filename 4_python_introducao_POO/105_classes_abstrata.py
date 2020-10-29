"""
    classes abstratas são classes genericas
    ex.:

    Cliente
        L Aluno
        L Cliente
"""

from classes.contapoupanca import ContaPoupanca


conta1 = ContaPoupanca(11111, 22222, 33333)
conta1.sacar(100)
print(conta1.saldo)