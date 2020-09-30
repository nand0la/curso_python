import dados

nova_lista_preco_almento = map(lambda item: item['preco'] * 1.5, dados.produtos)
for i in nova_lista_preco_almento:
    print(i)