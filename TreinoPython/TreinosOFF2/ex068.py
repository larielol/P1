import random
jogadas = 0
soma = 0
while True:
    escolha1 = int(input('Digite um valor: '))
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    escolhapc = random.choice(lista)
    escolha2 = ' '
    while escolha2 not in 'PI':
        escolha2 = input('Par ou impar? [P/I]: ').upper()[0]
    soma = escolha1 + escolhapc
    print(f'Você escolheu {escolha1} e o computador escolheu {escolhapc}, a soma entre eles é: {soma}')
    if escolha2 == 'P':
        if soma % 2 == 0:
            print(f'Você venceu!')
            jogadas += 1
        else:
            print('Você perdeu!')
            break
    if escolha2 == 'I':
        if soma % 2 != 0:
            print(f'Você ganhou!')
            jogadas += 1
        else:
            print('Você perdeu!')
            break
    print('Próxima rodada...')
print(f'Game over, você venceu {jogadas} vezes.')
