import random

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolhidos = (random.choice(numeros), random.choice(numeros),
              random.choice(numeros), random.choice(numeros),
              random.choice(numeros))

num = (escolhidos[0], escolhidos[1], escolhidos[2], escolhidos[3], escolhidos[4])

print(f'Os números sorteados foram: {num}')
print(f'O menor número da lista é: {min(num)}')
print(f'O maior número da lista é: {max(num)}')