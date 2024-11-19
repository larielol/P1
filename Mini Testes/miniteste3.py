conjuntos = []
conjuntoMaiorVogais = 0
quantidadeMaiorVogais = 0
conjuntoAtual = []
while True:
    palavra = input()

    if palavra == 'fim':
        conjuntos.append(conjuntoAtual)
        conjuntoAtual = None
        break

    if palavra == '---':
        conjuntos.append(conjuntoAtual)
        conjuntoAtual = []
    else:
        conjuntoAtual.append(palavra)

for indiceConjunto in range(len(conjuntos)):
    conjunto = conjuntos[indiceConjunto]
    vogais = 0

    for palavra in conjunto:
        for letra in palavra:
            if letra in 'aeiou':
                vogais += 1

    if vogais > quantidadeMaiorVogais:
        conjuntoMaiorVogais = indiceConjunto + 1
        quantidadeMaiorVogais = vogais

print(f'Conjunto {conjuntoMaiorVogais}: {quantidadeMaiorVogais} vogal(is)')
