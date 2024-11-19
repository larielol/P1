peso = float(input('Digite aqui seu peso: '))
altura = float(input('Digite aqui sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é {imc:.1f}: abaixo do peso')
elif imc >= 18.5 and imc <=25:
    print(f'Seu IMC é {imc:.1f}: peso ideal.')
elif imc > 25 and imc <= 30:
    print(f'Seu IMC é {imc:.1f}: sobrepeso.')
elif imc > 30 and imc <= 40:
    print(f'Seu IMC é {imc:.1f}: obesidade.')
else:
    print(f'Seu IMC é {imc:.1f}: obesidade mórbida.')