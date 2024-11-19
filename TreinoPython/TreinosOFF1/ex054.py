contmaior = 0
contmenor = 0
for n in range(1, 8):
    nasc = int(input(f'Em que ano a {n}° pessoa nasceu? '))
    idade = 2022 - nasc
    if idade <= 18:
        contmenor += 1
    else:
        contmaior += 1
print(f'Existe {contmenor} menores de idade e {contmaior} maiores de idade')