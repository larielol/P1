distancia = float(input('Qual a distância da viagem em Km/h? '))

valor1 = distancia * 0.50
valor2 = distancia * 0.45

if distancia <= 200:
    print(f"O valor da sua passagem é: R${valor1:.2f}.")
else:
    print(f"O valor da sua passagem é: R${valor2:.2f}.")

print('Boa viagem!')