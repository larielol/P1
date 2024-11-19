while 'F' or 'M':
    sexo = input('Digite seu sexo [M/F]: ').upper()[0]
    if sexo != 'F' and sexo != 'M':
        print('Sexo não reconhecido, tente novamente: ')
    elif sexo == 'F':
        sexo = 'feminino'
        print(f'Seu sexo é {sexo}!')
        break
    elif sexo == 'M':
        sexo = 'masculino'
        print(f'Seu sexo é {sexo}!')
        break


