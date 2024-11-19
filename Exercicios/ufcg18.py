def multiplica_lista(n, lista):
    tam = len(lista)
    lista_nova = []
    for i in range(n):
        for e in range(tam):
            lista_nova.append(lista[e])

    return lista_nova

nomes = ['joao', 'pedro']
#assert multiplica_lista(2, nomes) == ['joao', 'pedro', 'joao', 'pedro']
print(multiplica_lista(2, nomes))
