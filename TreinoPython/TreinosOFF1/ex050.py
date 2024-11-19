soma = 0
cont = 0

for i in range(0, 6):
    num = int(input())
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Números pares: {cont}, soma: {soma}')



