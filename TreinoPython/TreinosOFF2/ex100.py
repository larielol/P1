from random import randint

def sorteio(lista):
    for c in range(5):
        n = randint(1, 10)
        lista.append(n)
    print(f'Números sorteados: {numeros}')


def soma(lista):
    somaa = 0
    for i in lista:
        if i % 2 == 0:
            somaa += i
    print(f'A soma dos números pares é {somaa}')


numeros = []
sorteio(numeros)
soma(numeros)