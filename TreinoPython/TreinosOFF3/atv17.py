num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
print('Qual operação deseja realizar?')
print('Soma: 1')
print('Subtração: 2')
print('Multiplicação: 3')
print('Divisão: 4')
op = input('')

if op == '1':
    print('Operação escolhida: Soma (1).')
    numero = num1 + num2
    print(f'{num1} + {num2} = {numero}')
    if numero % 2 == 0:
        print(f'É par')
    else:
        print(f'É impar')
    if numero >= 0:
        print(f'É positivo')
    else:
        print(f'É negativo')
    if numero == round(numero):
        print(f'É inteiro')
    else:
        print(f'É decimal')
elif op == '2':
    print('Operação escolhida: Subtração (2).')
    numero = num1 - num2
    print(f'{num1} - {num2} = {numero}')
    if numero % 2 == 0:
        print(f'É par')
    else:
        print(f'É impar')
    if numero >= 0:
        print(f'É positivo')
    else:
        print(f'É negativo')
    if numero == round(numero):
        print(f'É inteiro')
    else:
        print(f'É decimal')
if op == '3':
    print('Operação escolhida: Multiplicação (3).')
    numero = num1 * num2
    print(f'{num1} x {num2} = {numero}')
    if numero % 2 == 0:
        print(f'É par')
    else:
        print(f'É impar')
    if numero >= 0:
        print(f'É positivo')
    else:
        print(f'É negativo')
    if numero == round(numero):
        print(f'É inteiro')
    else:
        print(f'É decimal')
elif op == '4':
    print('Operação escolhida: Divisão (4).')
    numero = num1 / num2
    print(f'{num1} / {num2} = {numero}')
    if numero % 2 == 0:
        print(f'É par')
    else:
        print(f'É impar')
    if numero >= 0:
        print(f'É positivo')
    else:
        print(f'É negativo')
    if numero == round(numero):
        print(f'É inteiro')
    else:
        print(f'É decimal')
else:
    print('Operação escolhida: inválida!')
    print('Verifique e tente novamente!')