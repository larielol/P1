lista = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    con = input('Quer continuar? [S/N] ').strip()[0]
    if con == 'N' or con == 'n':
        break

for i, a in enumerate(lista):
    print(f'Número: {i}, aluno: {a[0]} e média: {a[2]}')

while True:
    opc = int(input('Notas de qual aluno? (999 = break) '))
    if opc == 999:
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
