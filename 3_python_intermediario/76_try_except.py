"""
    tratando error

    quando usar try e quando usar if
    - 
"""

try:
    a = []
    print(a)
    print(a[1])
except NameError as error:
    print('o error foi: ', error)
except IndexError as error:
    print('error de indice')
except Exception as error:  # pega qualquer error do meu bloco
    print('qualquer error')
else: 
    print('executado quando não á erros')
finally:
    print('Sempre executados')

