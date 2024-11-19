menor_triplas = 0
soma = 0
lista_menores = []

while True:
    tripla = input()
    if tripla == 'fim':
        break
    if tripla[0] == tripla[2] == tripla[4]:
        break
    triplas = tripla.split()
    for i in range(len(triplas)):
        triplas[i] = int(triplas[i])
    for i in range(len(triplas)):
        menor_triplas = triplas[0]
        if menor_triplas > triplas[i]:
            menor_triplas = triplas[i]
    lista_menores.append(menor_triplas)

for ele in lista_menores:
    soma += ele
media = soma / len(lista_menores)

menor = lista_menores[0]
maior = lista_menores[0]

for i in range(len(lista_menores)):
    if menor > lista_menores[i]:
        menor = lista_menores[i]
    if maior < lista_menores[i]:
        maior = lista_menores[i]

if len(lista_menores) == 0:
    print(f'Média dos menores: nada')
    print(f'Menor entre os menores: nada')
    print(f'Maior entre os menores: nada')
else:
    print(f'Média dos menores: {media:.2f}')
    print(f'Menor entre os menores: {menor}')
    print(f'Meior entre os menores: {maior}')