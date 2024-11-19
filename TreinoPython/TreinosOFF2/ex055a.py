lista = []
for p in range(1, 6):
    peso = float(input(f'Peso da {p}° pessoa? '))
    lista += [peso]

pesomax = max(lista)
pesomin = min(lista)

print(f'O maior peso é {pesomax}KG e o menor peso é {pesomin}KG')