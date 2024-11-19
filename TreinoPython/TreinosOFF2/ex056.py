listaidade = []
maioridadehomem = 0
nomehomemvelho = ''
contmulher = 0


for np in range(1, 5):
    print(f'---- {np}° ----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()

    listaidade += [idade]

    if sexo == 'M':
        maioridadehomem = idade
        nomehomemvelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehomemvelho = nome

    if sexo == 'F' and idade <= 19:
        contmulher += 1

somaidade = listaidade[0] + listaidade[1] + listaidade[2] + listaidade[3]
mediaidade = somaidade / np


print(f'A média de idades do grupo é {mediaidade}.')
print(f'O homem mais velho se chama {nomehomemvelho} e tem {maioridadehomem} anos.')
print(f'Existe {contmulher} mulher(s) abaixo de 20 anos.')