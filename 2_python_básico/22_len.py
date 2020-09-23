user = input('Write your user name: ')
qtd_caracter = len(user)

if qtd_caracter <= 6:
    print('Não pode entrar')
else:
    print('Pode entrar')
