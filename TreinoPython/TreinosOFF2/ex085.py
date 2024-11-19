numeros = [[], []]

for n in range(7):
    num = int(input(f'Digite o {n+1}° número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0].sort()
print(f'Os valores pares: {numeros[0]}')
numeros[1].sort()
print(f'Os valores impares: {numeros[1]}')