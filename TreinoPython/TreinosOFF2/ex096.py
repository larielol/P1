def area(cal1, cal2):
    terreno = larg * alt
    print(f'A área de um terreno {larg}x{alt} é de {terreno}m².')


larg = float(input('Largura: '))
alt = float(input('Altura: '))
area(larg, alt)