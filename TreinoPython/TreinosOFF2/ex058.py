import random

print('Vamos jogar? Advinhe o número no qual eu estou pensando entre 0 e 5.')
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolhido = random.choice(lista)
acertou = False
somador = 0
while not acertou:
    jogador = int(input('Digite aqui o número entre 0 e 10: '))
    if jogador == escolhido:
        acertou = True
    somador += 1
print('Acertou!')
print(f'Foram {somador} tentativas.')