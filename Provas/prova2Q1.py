def pos_e_neg(numeros):
    numeros_ordenados = []
    for i in range(len(numeros)):
        if numeros[i] < 0:
            numeros_ordenados.append(numeros[i])
    for i in range(len(numeros)):
        if numeros[i] >= 0:
            numeros_ordenados.append(numeros[i])
    return numeros_ordenados

numeros = [-3, 9, 4, 0, -2, -8, 11]
pos_e_neg(numeros)
print(numeros)
