lista0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lista1 = ['Ferrnando', 123, True]
lista2 = ['a', 'b', 'c']

print(lista2[1])
print(lista2[1])

lista1[1] = '...'
print(lista1)

# append
lista1.append('adicionei no final')

# extend
lista0.extend(lista2)
print(lista0)

# pop
ultimo_item_lista = lista2.pop()
