contpar = 0
cont9 = 0
for i in range(1):
    num = (int(input('Digite um número: ')), int(input('Digite um número: ')),
           int(input('Digite um número: ')), int(input('Digite um número: ')))
    if num == 9:
        cont9 += 1
    for n in num:
        if n % 2 == 0:
            contpar += 1
print(cont9)
print(f'O 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro 3 está na posição {num.index(3)+1}°')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram {contpar}')