numeros = []
posicao_maior = []
posicao_menor = []
for n in range(0, 5):
    num = int(input(f'Digite um número na posição {n}: '))
    numeros.append(num)
for posicao, numero in enumerate(numeros):
    if numero == max(numeros):
        posicao_maior.append(posicao)
    if numero == min(numeros):
        posicao_menor.append(posicao)


print(f'Você digitou os valores {numeros}')
print(f'O maior valor é {max(numeros)} na posição {posicao_maior}...')
print(f'O menor valor é {min(numeros)} na posição {posicao_menor}...')


# print(f'O maior valor é {max(numeros)} na posição {numeros.index(max(numeros))}')
# print(f'O menor valor é {min(numeros)} na posição {numeros.index(min(numeros))}')