import dados
from functools import reduce

soma_lista = reduce(lambda ac, i: i + ac, dados.lista, 0)
print(soma_lista)

