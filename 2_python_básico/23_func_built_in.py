num1 = input('Digite um numero: ')
num2 = input('Digite um numero: ')

if num1.isdigit() and num2.isdigit():
    print(f'soma: {int(num1) + int(num2)}')
else:
    if not num1.isdigit() or not num2.isdigit():
        print(f'{num1} | {num2} não é um numero')