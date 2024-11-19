num = int(input('Termos? '))
f = 0
s = 1
cont = 2
print(f'{f} -> {s}', end='')
while cont <= num:
    numero = f + s
    print(f'{numero} -> ', end= '')
    f = s
    s = numero
    cont += 1
print('Acabou')
