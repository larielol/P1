quant_vogais = 0
conjunto_numero = 0
lista_quant_vogais = []
lista_conjuntos = []

while True:
    palavra = input()
    if palavra == 'fim':
        break
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            quant_vogais += 1
    if palavra == '---':
        conjunto_numero += 1
        lista_quant_vogais.append(quant_vogais)
        lista_conjuntos.append(conjunto_numero)
        quant_vogais = 0

conjunto_maior = lista_conjuntos[0]
numero_vogais = lista_quant_vogais[0]
for i in range(len(lista_quant_vogais)):
    if numero_vogais < lista_quant_vogais[i]:
        numero_vogais = lista_quant_vogais[i]
        conjunto_maior = lista_conjuntos[i]

print(f'Conjunto {conjunto_maior}: {numero_vogais} vogal(is)')
