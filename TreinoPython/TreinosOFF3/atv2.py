nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))

media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
    print('Aprovado')
elif media < 7:
    print('Reprovado')
else:
    print('Aprovado com distinção')
