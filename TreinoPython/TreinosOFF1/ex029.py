velocidade = float(input('Velocidade atual em Km/h: '))

multa = (velocidade - 80) * 7

if velocidade <= 80:
    print('Você está na velocidade permitida.')
else:
    print('Você ultrapassou a velocidade permitida e foi multado.')
    print(f'O valor da multa é: R${multa:.2f}')
