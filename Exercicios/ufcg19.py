def encontra_menores(num, lista):
    menor = 0
    for i in range(len(lista)):
        if num > lista[i]:
            menor = lista[i]
            break
    if menor == 0:
        menor = -1
    return menor


lista1 = [100, 200, 300, 400]
lista2 = [15, 12, 4, 9, 10]
assert encontra_menores(100, lista1) == -1
assert encontra_menores(10, lista2) == 4

lista1 = [100, 200, 300, 400]
encontra_menores(100, lista1)
lista2 = [15, 12, 4, 9, 10]
encontra_menores(10, lista2)