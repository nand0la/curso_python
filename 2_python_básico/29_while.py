# '''
#     - repeticao

#     while condicao:
#         faça isso
# '''

# x = 0
# while x < 100:
#     if x == 3:
#         x += 1
#         print('PULEI O 3')
#         continue

#     print(x)
#     x += 1
# else:
#     print('A repeticao acabou')


texto = "Fernando"

i = 0
nova_frase = ""
while i < len(texto):
    nova_frase += texto[i]
    print(nova_frase)
    i += 1
