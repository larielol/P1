lista = []
num = int(input())
numeros = input().split()
lista.append(numeros)
for num in lista:
    if num in lista:
        print(f'sim')
    else:
        print(f'não')
