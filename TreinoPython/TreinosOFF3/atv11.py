import math

a = int(input("Valor de A: "))

if a == 0:
    print("Equação não é do segundo grau")
else:
    b = int(input("Valor de B: "))
    c = int(input("Valor de C: "))
    delta = b**2 - 4 * a * c

    if delta < 0:
        print('A equação não possui raízes')
    elif delta == 0:
        print('A equação possui apenas uma raíz real')
    else:
        print('A equação possui duas raízes reais')