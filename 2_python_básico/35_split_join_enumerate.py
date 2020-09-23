'''
    - split
    - join
    - enumerate
'''

string = 'Uma frase muito grande aqui amigão fica esperto em'
lista = string.split(' ')
print(lista)

for palavra in lista:
    print(f'a palavra {palavra} apareceu {lista.count(palavra)}x na lista')

lista_palavra = ' '.join(lista)
print(lista_palavra)

print()
print()
print()

for i, j in enumerate(lista):
    print(i, j)