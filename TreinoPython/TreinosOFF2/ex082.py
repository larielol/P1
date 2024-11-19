numeros = []
pares = []
impares = []
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    con = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if con == 'N' or con == 'n':
        break
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Lista: {numeros}')
print(f'Lista com os números pares: {pares}')
print(f'Lista com os números impares: {impares}')
