num = int(input())
numeros = input().split()
cont = 0
for elemento in numeros:
    if num == int(elemento):
        cont += 1
    else:
        cont += 0
if cont >= 1:
    print(f'sim')
else:
    print(f'não')