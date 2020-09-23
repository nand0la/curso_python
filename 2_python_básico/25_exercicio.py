# programa 1
numero_inteiro = input('Digite um numero inteiro: ')

if numero_inteiro.isnumeric():

    numero_inteiro = int(numero_inteiro)

    if numero_inteiro % 2 == 0:
        print('Par')

    else:
        print('Impar')

else:
    print('Digite um numero inteiro')



# programa 2
hora = input('Digite a hora: ')

if hora.isnumeric():
    hora = int(hora)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 18:
        print('Boa tarde')
    elif hora >= 19 and hora <= 23:
        print('Boa noite')

else:
    print('Digite a hora inteira')



# programa 3
nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('nome curto')
elif len(nome) == 5 or len(nome) == 6:
    print('nome normal')
elif len(nome) >= 6:
    print('nome grande')

