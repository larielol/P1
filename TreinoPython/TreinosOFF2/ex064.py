cont = num = 0
num = int(input('Digite o número 999 para parar: '))
while num != 999:
    cont += num
    num = int(input('Digite o número 999 para parar: '))
print(f'A soma dos números digitados é: {cont}.')