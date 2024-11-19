import random

nome1 = input('Digite aqui o primeiro nome: ')
nome2 = input('Digite aqui o segundo nome: ')
nome3 = input('Digite aqui o terceiro nome: ')
nome4 = input('Digite aqui o quarto nome: ')

lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)

print(f"O nome escolhido é:  {escolhido}.")
