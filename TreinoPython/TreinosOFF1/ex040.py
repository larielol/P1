nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'Sinto muito, você foi reprovado! Sua média foi {media:.1f}.')
elif media > 5.0 and media < 6.9:
    print(f'Você está na recuperação, estude! Sua média é {media:.1f}.')
elif media > 7.0:
    print(f'Parabéns, você foi aprovado! Sua média foi {media:.1f}.')