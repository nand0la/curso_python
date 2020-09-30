import sys

"""
    diferente das listas, os geradores é um iteravel e iterador
    ele vai te retornar um valor de cada vez
"""

# def gera():
#     for n in range(100):
#         yield n

gerador1 = (x for x in range(1000))
gerador2 = [x for x in range(1000)]

print(sys.getsizeof(gerador1))
print(sys.getsizeof(gerador2))

