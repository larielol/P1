frase = input('Frase: ').strip().lower()
p = frase.split()
junto = ''.join(p)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Palíndromo')
else:
    print('Não é palíndromo')