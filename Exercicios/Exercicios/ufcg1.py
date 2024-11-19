voluntario1 = input('')
voluntario2 = input('')
voluntario3 = input('')

if voluntario1[0] < voluntario2[0] and voluntario1[0] < voluntario3[0]:
    print(f'{voluntario1} (1)')
elif voluntario1[0] == voluntario2[0] or voluntario1[0] == voluntario3[0]:
    print(f'{voluntario1} (2)')
elif voluntario2[0] < voluntario1[0] and voluntario2[0] < voluntario3[0]:
    print(f'{voluntario2} (1)')
elif voluntario2[0] == voluntario3[0] and voluntario2[0] != voluntario1[0]:
    print(f'{voluntario2} (2)')
elif voluntario3[0] < voluntario1[0] and voluntario3[0] < voluntario2[0]:
    print(f'{voluntario3} (1)')
else:
    print(f'{voluntario3} (2)')
