num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

if num1 > num2 and num1 > num3:
    print(f'O maior número é {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O maior número é o {num2}')
else:
    print(f'O maior número é o {num3}')