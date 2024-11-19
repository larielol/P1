from time import sleep
from random import randint
jogos = int(input('Quantos jogos? '))
lista = []
lista_jogos = []
total = 1
while total <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >=6:
            break
    lista.sort()
    lista_jogos.append(lista[:])
    lista.clear()
    total += 1
for i, l in enumerate(lista_jogos):
    print(f'Jogo {i+1}: {l}')