import random
import time

print('Vamos jogar Jokenpô?')
print('Escolha: pedra, papel ou tesoura.')
print('='*40)
jogador = input('Digite aqui sua escolha: ').upper()

lista = ['PEDRA', 'PAPEL', 'TESOURA']
escolhido = random.choice(lista)

print('-' * 10)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ!!!')
time.sleep(1)
print('-' * 10)

if escolhido == jogador:
    print(f'Empate! Eu escolhi {escolhido} e você {jogador}.')
elif escolhido == 'PEDRA' and jogador == 'TESOURA':
    print(f'Eu ganhei! Eu escolhi {escolhido} e você {jogador}.')
elif escolhido == 'TESOURA' and jogador == 'PEDRA':
    print(f'Você ganhou! Eu escolhi {escolhido} e você {jogador}.')
elif escolhido == 'PAPEL' and jogador == 'TESOURA':
    print(f'Você ganhou! Eu escolhi {escolhido} e você {jogador}.')
elif escolhido == 'TESOURA' and jogador == 'PAPEL':
    print(f'Eu ganhei! Eu escolhi {escolhido} e você {jogador}.')
elif escolhido == 'PEDRA' and jogador == 'PAPEL':
    print(f'Você ganhou! Eu escolhi {escolhido} e você {jogador}.')
elif escolhido == 'PAPEL' and jogador == 'PEDRA':
    print(f'Eu ganhei! Eu escolhi {escolhido} e você {jogador}.')
else:
    print(f'Escolha não reconhecida, tente novamente.')
