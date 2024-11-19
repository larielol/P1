num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

if num1 < num2 and num1 < num3 and num2 < num3:
    print(f'A sequencia decrescente é: {num3}, {num2} e {num1}')
elif num1 < num2 and num1 < num3 and num2 > num3:
    print(f'A sequencia decrescente é: {num2}, {num3} e {num1}')
elif num2 < num1 and num2 < num3 and num1 < num3:
    print(f'A sequencia decrescente é: {num3}, {num1} e {num2}')
elif num2 < num1 and num2 < num3 and num1 > num3:
    print(f'A sequencia decrescente é: {num1}, {num3} e {num2}')
elif num3 < num1 and num3 < num2 and num1 < num2:
    print(f'A sequencia decrescente é: {num2}, {num1} e {num3}')
else:
    print(f'A sequencia decrescente é: {num1}, {num2} e {num3}')