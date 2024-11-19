import random

print('Vamos jogar? Advinhe o número no qual eu estou pensando entre 0 e 5.')
num = input('Digite aqui o número entre 0 e 5: ')

lista = ['0', '1', '2', '3', '4', '5']
escolhido = random.choice(lista)

if escolhido == num:
    print('Parabéns, você ganhou!')
    print('A resposta é:', escolhido)
else:
    print('Que pena, eu ganhei!')
    print('A resposta era:', escolhido)
