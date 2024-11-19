num = int(input())

cont = num
f = 1
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print(f'{f}')