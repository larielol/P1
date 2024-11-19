barato = ''
soma = produto = soma1k = menor = 0
while True:
    nome = input('Produto? ')
    preco = float(input('Preço? '))
    soma += preco
    produto += 1
    continuar = input('Deseja continuar? [S/N] ').upper()[0]
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').upper()[0]
    if continuar == 'N':
        break
    if preco > 1000:
        soma1k += 1
    if produto == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
print('-' * 50)
print(f'Total gasto: R${soma}')
print(f'Produtos que custam mais de R$1000: {soma1k}')
print(f'Produto mais barato: {barato}, que custa: R${menor}')