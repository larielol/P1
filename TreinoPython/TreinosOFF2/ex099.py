def maior(* num):
    cont = maior = 0
    print(f'\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor}')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Total de valores: {cont}', end='')
    print()
    print(f'Maior: {maior}', end='')
    print()

maior(2, 9, 4, 5, 7, 1)
maior(2, 9, 4)
maior(4, 5)
maior(8)
maior()