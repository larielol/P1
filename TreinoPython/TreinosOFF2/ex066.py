num = soma = cont = 0
while True:
    num = int(input('Digite números [999: PARAR!]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} valores foi {soma}!')