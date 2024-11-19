def soma_intervalo(a, b):
    cont = 0
    soma = 1
    for n in range(a-1, b):
        n += soma
        soma += 0
        cont += n
        print(cont)


print(soma_intervalo(5, 15))
#assert soma_intervalo(5, 15) == 110
