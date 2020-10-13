"""
    funcao decoradoras
    - usadas para envolver funcoes e mudar seu comportamento
"""

# estrutura decorador

def decora(func):
    def decorador():
        print('===========')
        func()
        print('###########')

    return decorador


@decora
def quero_decorar():
    print('ola')


quero_decorar
