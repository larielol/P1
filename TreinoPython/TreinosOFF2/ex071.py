valor = int(input('Qual o valor que tu queres sacas? R$ '))
saque = valor
nota = 50
totalnotas = 0

while True:
    if saque >= nota:
        saque -= nota
        totalnotas += 1
    else:
        print(f'{totalnotas} notas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totalnotas = 0
        if saque == 0:
            break