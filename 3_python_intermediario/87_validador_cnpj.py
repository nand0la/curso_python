"""
    52.875.878/0001-74 || 27.885.558/0001-58 || 71.832.708/0001-57

    5  2  8  7  5  8  7  8  0  0  0  1  x  x
    5  4  3  2  9  8  7  6  5  4  3  2 
    25 8  24 14 45 64 49 48 0  0  0  2 = 279
    
    11 - (279 % 11) = 7
"""

CNPJ = "52.875.878/0001-74"

def retorna_cnpj_limpo(cnpj):
    cnpj_limpo = cnpj.replace("-", "")
    cnpj_limpo = cnpj_limpo.replace(".", "")
    cnpj_limpo = cnpj_limpo.replace("/", "")

    return cnpj_limpo


# GERANDO O PRIMEIRO DIGITO
def retorna_primeiro_digito(CNPJ):
    LISTA_VALORES = [int(numero) for numero in retorna_cnpj_limpo(CNPJ)]
    LISTA_SOMA = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    LISTA_TUPLA_SOMAS = zip(LISTA_VALORES, LISTA_SOMA)
    LISTA_TUPLA_MULTIPLICADA = sum([x * y for x, y in LISTA_TUPLA_SOMAS])

    PRIMEIRO_DIGITO = 11 - (LISTA_TUPLA_MULTIPLICADA % 11)
    return PRIMEIRO_DIGITO if PRIMEIRO_DIGITO <= 9 else 1


def retorna_segundo_digito(CNPJ):
    LISTA_VALORES = [int(numero) for numero in retorna_cnpj_limpo(CNPJ)]
    LISTA_SOMA = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    LISTA_TUPLA_SOMAS = zip(LISTA_VALORES, LISTA_SOMA)
    LISTA_TUPLA_MULTIPLICADA = sum([x * y for x, y in LISTA_TUPLA_SOMAS])
    
    SEGUNDO_DIGITO = 11 - (LISTA_TUPLA_MULTIPLICADA % 11)
    return SEGUNDO_DIGITO if SEGUNDO_DIGITO <= 9 else 1



while True:
    print()
    input_cnpj = input('Digite o cnpj: ')

    cnpj_limpo = retorna_cnpj_limpo(input_cnpj)
    cnpj_validar = f"{cnpj_limpo[:12]}{retorna_primeiro_digito(cnpj_limpo)}{retorna_segundo_digito(cnpj_limpo)}"

    if cnpj_limpo == cnpj_validar:
        print('Validado')
    else:
        print('Invalido')
