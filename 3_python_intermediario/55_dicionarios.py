d1 = {
    'chave1' : 'valor da chave',
    'chave2' : 'valor da nova chave',
}

print(d1['chave1'])
print(d1.get('chave_que_n_existe'))

print('chave1' in d1.keys())
print('valor da chave' in d1.values())

for key, values in d1.items():
    print(f'{key}: {values}')

lista_chave_e_valor = [
    ['k1', 'v1'],
    ['k2', 'v2'],
    ['k3', 'v3'],
    ['k4', 'v4'],
    ['k5', 'v5'],
]

print(dict(lista_chave_e_valor))
