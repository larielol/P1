limite = int(input())
limite_max = limite * 5
lista_numeros = []
lista_soma = []
soma = 0
while True:
    numeros = input()
    soma = 0
    if numeros == '-':
        break
    valores = numeros.split()
    for i in range(len(valores)):
        if int(valores[i]) != 0:
            soma += int(valores[i])
            lista_numeros.append(int(valores[i]))
    lista_soma.append(soma)
    if soma > limite_max:
        break
for item in lista_numeros:
    print(f'{item} {soma}')