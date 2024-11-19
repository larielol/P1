print('Turnos: M = Matutino, V = Vespertino e N = Noturno.')
turno = input('Em qual turno você estuda? ').upper()

if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Turno inválido, verifique e tente novamente.')
