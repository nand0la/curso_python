lista1 = [1, 2, 3, 4, 5, 6, 3, 4, 5, 6]
lista2 = [1, 2, 3, 4, 5, 6]

lista_zip = [sum(tupla_values) for tupla_values in zip(lista1,lista2)]
print(lista_zip)
