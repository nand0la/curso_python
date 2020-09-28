pontos = 0
pergunta_resposta = {
    'Pergunta 1' : {
        'pergunta' : 'Quanto e 2 + 2?',
        'respostas' : {
            'a' : 2,
            'b' : 1,
            'c' : 4,
        },
        'resposta certa' : 'c'
    },

    'Pergunta 2' : {
        'pergunta' : 'Quanto e 3 + 2?',
        'respostas' : {
            'a' : 2,
            'b' : 5,
            'c' : 4,
        },
        'resposta certa' : 'b'
    },
}


for key, value in pergunta_resposta.items():
    print(value['pergunta'])

    for key_pergunta, value_pergunta in value['respostas'].items():        
        print(f'{key_pergunta}) {value_pergunta}')


    resposta = input('Digite a resposta: ')
    if resposta == value['resposta certa']:
        pontos += 1
        print(f'acertou voce esta com {pontos} pontos')
    else:
        print('errou')

    print()
