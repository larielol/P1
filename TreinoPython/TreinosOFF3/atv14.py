num = int(input('Digite um número menor que 1000: '))

if num >= 1000:
    print('Número maior que mil!')
elif num < 1000 and num >=100:
    unidade = num % 10
    num1 = (num - unidade) / 10
    (dezena) = num1 % 10
    num2 = (num1 - dezena) / 10
    (centena) = num2
    print(f'{num} = {int(centena)} centenas, {int(dezena)} dezenas e {unidade} unidades')
else:
    unidade = num % 10
    num1 = (num - unidade) / 10
    dezena = num1 % 10
    print(f'{num} = {int(dezena)} dezenas e {unidade} unidades')
