lista = []
while True:
    palavra = input()
    contvogal = contconsoante = 0
    lista.append(palavra)
    for letra in palavra:
        if letra in "aeiouAEIOU":
            contvogal += 1
    print(f'{contvogal}')
    for letra in palavra:
        if letra not in "aeiouAEIOU":
            contconsoante += 1
    print(f'{contconsoante}')
    if contvogal < contconsoante:
        break

print(f'{len(lista)}')
