criterio_vogais = 0
criterio_consecutivas = 0

senha = input()
for i in range(len(senha)):
    if senha[i] in 'aeiou':
        criterio_vogais += 1
        if criterio_vogais == 6:
            print(f'Chave insegura. {criterio_vogais} vogais.')
            break
    if i < len(senha) - 2:
        if senha[i] == senha[i + 1] and senha[i] == senha[i+2]:
            criterio_consecutivas += 1
            if criterio_consecutivas == 3:
                print(f'Chave insegura. {criterio_consecutivas} caracteres iguais.')
                break

if criterio_vogais < 6 and criterio_consecutivas < 3:
    print(f'Chave segura!')