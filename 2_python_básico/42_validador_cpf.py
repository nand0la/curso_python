CPF = '168.995.350-09'


# limpando cpfs
cpf_multiplica_1 = CPF[:11].replace('.', '')
cpf_multiplica_2 = CPF[:13].replace('.', '').replace('-', '')


# gerando primeiro valor
multiplicador = 10
soma_primeiro_valor = 0

for numero in cpf_multiplica_1:
    soma_primeiro_valor += int(numero) * multiplicador
    multiplicador -= 1

primeiro_digito = 11 - (soma_primeiro_valor % 11)
primeiro_valor_final = primeiro_digito if primeiro_digito <= 9 else 0

print(primeiro_valor_final)



# gerando segundo valor
multiplicador2 = 11
soma_segundo_valor = 0

for numero in cpf_multiplica_2:
    soma_segundo_valor += int(numero) * multiplicador2
    multiplicador2 -= 1

segundo_digito = 11 - (soma_segundo_valor % 11)
segundo_valor_final = segundo_digito if segundo_digito <= 9 else 0

print(segundo_valor_final)

novo_cpf = f'{cpf_multiplica_1}{primeiro_valor_final}{segundo_valor_final}'
cpf_limpo = CPF.replace('.', '').replace('-', '')

print()
print()
print()

validado = True if novo_cpf == cpf_limpo else False
print(validado)