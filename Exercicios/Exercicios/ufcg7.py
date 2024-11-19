senha = input()
senhanova = ''
cont = 0

for i in range(len(senha)):
    if i != 0:
        if senha[i] == 'a' or senha[i] == 'A':
            senhanova += '4'
            cont += 1
        elif senha[i] == 'e' or senha[i] == 'E':
            senhanova += '3'
            cont += 1
        elif senha[i] == 'i' or senha[i] == 'I':
            senhanova += '1'
            cont += 1
        elif senha[i] == 'o' or senha[i] == 'O':
            senhanova += '0'
            cont += 1
        else:
            senhanova += senha[i]
    else:
        senhanova += senha[i]
print(f'{senhanova} ({cont} troca(s))')