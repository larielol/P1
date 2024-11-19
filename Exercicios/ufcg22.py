# Programação 1, 2021.2
# Solução de "Entre os extremos"
# lucas.ariel.carvalho@ccc.ufcg.edu.br

lista_extremos = []
lista_numeros = []
lista_intervalo = []
numeros_extremos = ''

while True:
    num = input()
    if num == 'fim':
        break
    valores = num.split()
    for i in range(len(valores)):
        if int(valores[i]) != 'fim':
            lista_numeros.append(int(valores[i]))

for j in range(len(lista_numeros)):
    if j == 0:
        lista_extremos.append(lista_numeros[j])
    elif j == len(lista_numeros) - 1:
        lista_extremos.append(lista_numeros[j])

maior = lista_extremos[0]
menor = lista_extremos[1]
if maior < menor:
    maior = lista_extremos[1]
    menor = lista_extremos[0]

for n in range(len(lista_numeros)):
    if lista_numeros[n] < maior and lista_numeros[n] > menor:
        lista_intervalo.append(lista_numeros[n])

for e in range(len(lista_extremos)):
    if e == len(lista_extremos) - 1:
        numeros_extremos += f'{lista_extremos[e]}'
        print(numeros_extremos)
    else:
        numeros_extremos += f'{lista_extremos[e]} '

for c in lista_intervalo:
    print(c)
