primeiro = int(input())
razao = int(input())
cont = 1
total = 0
termos = 10
while termos != 0:
    total += termos
    while cont < total:
        print(f'{primeiro} ', end='')
        primeiro += razao
        cont += 1

    print('PAUSA')
    termos = int(input('Quantos termos você quer mostrar a mais? '))
print('Hasta la vista')
print(f'Total de termos mostrados foi: {cont}')