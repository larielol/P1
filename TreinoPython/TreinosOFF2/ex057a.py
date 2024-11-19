sexo = input('Digite seu sexo [F/M]: ').upper()[0]
while sexo not in 'MmFf':
    sexo = input('Sexo não reconhecido, tente novamente: ')
print(f'Sexo {sexo}!')