numeros = []
while True:
    num = int(input('Digite um valor: '))
    numeros.append(num)
    con = input('Quer continuar? [S/N] ')[0]
    if con == 'N' or con == 'n':
        break

print(f'Foram digitados {len(numeros)} números')
numeros.sort(reverse=True)
print(f'A ordem decrescente da lista é: {numeros}')
if 5 in numeros:
    print(f'O valor 5 foi digitado')
else:
    print(f'O valor 5 não foi digitado')