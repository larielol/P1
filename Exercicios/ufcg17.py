media = float(input())
media_minima = media / 2
soma = 0
lista_numeros = []
while True:
    numero = input()
    if numero == 'fim':
        break
    numeros = numero.split()
    for i in range(len(numeros)):
        if int(numeros[i]) != 0:
            soma += int(numeros[i])
    media_numeros = soma / (len(numeros))
    if media_numeros > media:
        lista_numeros.append(numero)
    if media_numeros < media_minima:
        break
    soma = 0
for item in lista_numeros:
    print(item)