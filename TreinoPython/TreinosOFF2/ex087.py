lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma1 = soma2 = soma3 = 0
for l in range(3):
    for c in range(3):
        lista[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

for l in range(3):
    for c in range(3):
        print(f'[{lista[l][c]:^5}]', end='')
        if lista[l][c] % 2 == 0:
            soma1 += lista[l][c]
    print()
print(f'A soma dos pares é {soma1}')
for l in range(3):
    soma2 += lista[l][2]
print(f'Soma dos elementos da terceira coluna: {soma2}')
for c in range(3):
    if c == 0:
        soma3 = lista[1][c]
    elif lista[1][c] > soma3:
        soma3 = lista[1][c]
print(f'Soma da terceira linha: {soma3}')