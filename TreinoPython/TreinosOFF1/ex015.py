kmp = float(input('Quilometragem percorrida? '))
aluguel = int(input('Quantidade de dias alugado? '))

precoa = aluguel * 60
precok = kmp * 0.15

precot = precoa + precok

print(f"O preço pelos dias alugados será: R${precoa}")
print(f"O preço pelos quilometros percorridos será: R${precok}")
print(f"O preço total a pagar será: R${precot:.2f}!")
