somahomem = somamulher = maiorhomem = menorhomem = maiormulher = menormulher = 0
while True:
    idade = int(input('Idade: '))
    sexo = (input('Sexo: [M/F] ')).upper()
    while sexo not in 'MF':
        sexo = (input('Sexo: [M/F] ')).upper()
    continuar = input('Deseja continuar? [S/N] ').upper()
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').upper()
    if sexo == 'F':
        somamulher += 1
        if idade < 18:
            menormulher += 1
        else:
            maiormulher += 1
    elif sexo == 'M':
        somahomem += 1
        if idade < 18:
            menorhomem += 1
        else:
            maiorhomem += 1
    if continuar == 'N':
        break

somamaior = maiorhomem + maiormulher
print(f'Total de pessoas com mais de dezoito anos: {somamaior}')
print(f'Ao todo temos {somahomem} homens cadastrados')
print(f'E temos {menormulher} mulheres com menos de 20 anos')