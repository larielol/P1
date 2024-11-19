lista = []
lista_auxiliar = []
pessoasc = 0
maior = menor = 0

while True:
    nome = input('Digite o nome: ')
    peso = float(input('Digite o peso: '))
    lista_auxiliar.append(nome)
    lista_auxiliar.append(peso)
    pessoasc += 1
    if len(lista) == 0:
        maior = menor = lista_auxiliar[1]
    else:
        if lista_auxiliar[1] > maior:
            maior = lista_auxiliar[1]
        if lista_auxiliar[1] < menor:
            menor = lista_auxiliar[1]
    lista.append(lista_auxiliar[:])
    lista_auxiliar.clear()
    continuar = input('Deseja continuar? [S/N] ').strip()[0]
    if continuar == 'N' or continuar == 'n':
        break

print(f'Ao todo, você cadastrou {pessoasc} pessoas')
print(f'O maior peso foi de {max(lista)}kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {min(lista)}kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print()