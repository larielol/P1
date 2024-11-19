distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia}')
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'E o preço da sua viagem será de R${preco:.2f}')