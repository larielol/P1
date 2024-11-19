def maioridade_penal(nome, idade):
    ano = idade.split()
    pessoa = nome.split()
    lista_maiores = []
    maiores = ''
    for i in range(len(ano)):
        if int(ano[i]) >= 18:
            lista_maiores.append(f'{pessoa[i]}')
    for i in range(len(lista_maiores)):
        if i == len(lista_maiores) - 1:
            maiores += f'{lista_maiores[i]}'
        else:
            maiores += f'{lista_maiores[i]} '

    return maiores

setor1 = maioridade_penal("Jansen Italo Ana", "14 21 60")
print(setor1)
# maioridade_penal("Jansen Italo Ana","14 21 60") == "Italo Ana"

