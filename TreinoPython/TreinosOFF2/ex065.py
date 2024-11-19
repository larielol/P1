cont = num = soma = maior = menor = 0
con = 's'
while con in 's':
    num = int(input('Digite um número: '))
    con = input('Quer continuar? [S/N] ').lower().strip()[0]
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont += 1
    soma += num
print(f'Você digitou {cont} número(s) e a média entre eles é: {soma/cont}')
print(f'O maior número é: {maior}, e o menor número é: {menor}')