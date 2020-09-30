from itertools import count, combinations

contador = count()

for i in contador:
    print(i)

    if i == 100:
        break


pessoa = ['Nando', 'Jose', 'Ana', 'Fabricio']
for group in combinations(pessoa, 2):
    print(group)