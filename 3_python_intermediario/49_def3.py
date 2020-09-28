def foo(*args, **kwargs):
    print(args)
    print(kwargs)

    idade = kwargs.get('idade')


'''
    *desempacotamento\empacotamento
    item1, item2 = lista
'''

foo(*[1, 2, 3, 4, 5, 6, 7], 'outro indice', )
