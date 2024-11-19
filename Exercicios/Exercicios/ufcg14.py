reprovados = 0
while True:
    aluno = input()
    if aluno == '-':
        break
    cont = 0
    falta = 0
    while cont < len(aluno):
        if aluno[cont] == "f":
            falta += 1
        cont += 1
    if falta > 8:
        reprovados += 1

print(f'{reprovados} aluno(s) reprovado(s) por falta.')