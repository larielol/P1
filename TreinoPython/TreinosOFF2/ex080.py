numeros = []
indice = 0
for n in range(0, 5):
    num = int(input('Digite um valor: '))
    if n == 0 or num > numeros[-1]:
        numeros.append(num)
    else:
        posicao = 0
        while posicao < len(numeros):
            if num <= numeros[posicao]:
                numeros.insert(posicao, num)
                break
            posicao += 1
print(f'Os valores digitados em ordem crescente são {numeros}')