numeros1 = []
while True:
    num = int(input('Digite um valor: '))
    if num not in numeros1:
        numeros1.append(num)
        print(f'Valor adicionado com sucesso...')
    else:
        print(f'Valor duplicado!')
    continuar = input('Quer continuar? [S/N] ')[0]
    if continuar == 'N' or continuar == 'n':
        break

print(f'Os valores digitados são {numeros1}')
numeros1.sort()
print(f'Em ordem crescente será {numeros1}')